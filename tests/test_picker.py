"""Behavioral regression tests; Python's standard library only."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]


class PickerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='ideonomy test ')
        self.root = Path(self.tmp.name)
        self.skill = self.root / 'standalone skill'
        shutil.copytree(REPO / 'ideonomy-plain', self.skill)

    def tearDown(self):
        self.tmp.cleanup()

    def run_pick(self, *args, skill=None):
        return subprocess.run(['bash', str((skill or self.skill) / 'bin/pick'), *args],
                              cwd=self.root, capture_output=True, text=True)

    def picks(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        return re.findall(r'^  - (.+)$', result.stdout, re.M)

    def snapshot(self):
        return {str(p.relative_to(self.skill)): (p.read_bytes(), p.stat().st_mtime_ns)
                for p in self.skill.rglob('*') if p.is_file()}

    def test_tuple_sizes_and_no_duplicates(self):
        for flags, expected in [((), 6), (('--less',), 4), (('--more',), 10)]:
            with self.subTest(flags=flags):
                result = self.run_pick('--seed', '42', '--print', *flags)
                self.assertEqual(len(self.picks(result)), expected)
                for block in re.split(r'\n\n', result.stdout)[1:-1]:
                    names = re.findall(r'^  - (.+)$', block, re.M)
                    self.assertEqual(len(names), len(set(names)))

    def test_seed_replay_and_leading_zero(self):
        first = self.run_pick('--seed', '42', '--print')
        self.assertEqual(self.picks(first), self.picks(self.run_pick('--seed', '00042', '--print')))
        self.assertEqual(first.stdout, self.run_pick('--seed', '42', '--print').stdout)
        self.picks(self.run_pick('--seed', '0'))
        self.picks(self.run_pick('--seed', '32767'))

    def test_multiple_seeds_vary(self):
        tuples = {tuple(self.picks(self.run_pick('--seed', str(n), '--print'))) for n in range(12)}
        self.assertGreater(len(tuples), 1)

    def test_rejects_malformed_arguments(self):
        for args in [('--seed',), ('--seed', ''), ('--seed', '2+2'), ('--seed', '-1'),
                     ('--seed', '32768'), ('--seed', '999999999999999999'),
                     ('--cooldown-dir',), ('--cooldown-dir', ''),
                     ('--cooldown-dir', '--print'), ('--random-org',), ('--wat',)]:
            with self.subTest(args=args):
                result = self.run_pick(*args)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, '')

    def test_default_and_seeded_runs_do_not_mutate_installation(self):
        before = self.snapshot()
        self.picks(self.run_pick('--print'))
        self.picks(self.run_pick('--seed', '42'))
        self.assertEqual(self.snapshot(), before)

    def test_history_is_separate_and_seeded_run_ignores_it(self):
        before = self.snapshot()
        history = self.root / 'usage history'
        self.picks(self.run_pick('--print', '--cooldown-dir', str(history)))
        entries = [p for p in history.rglob('*.md')]
        self.assertEqual(len(entries), 6)
        self.assertEqual(self.snapshot(), before)
        stamps = {p: p.stat().st_mtime_ns for p in entries}
        actual = self.run_pick('--seed', '42', '--print', '--cooldown-dir', str(history))
        self.assertEqual(actual.stdout, self.run_pick('--seed', '42', '--print').stdout)
        self.assertEqual(stamps, {p: p.stat().st_mtime_ns for p in entries})
        unused = self.root / 'must not be created'
        self.picks(self.run_pick('--seed', '42', '--cooldown-dir', str(unused)))
        self.assertFalse(unused.exists())

    def test_cooldown_penalizes_recent_methods(self):
        history = self.root / 'history'
        expected = []
        for category, count in [('operators', 2), ('organons', 1), ('dimension-prompts', 3)]:
            paths = sorted((self.skill / 'methods' / category).glob('*.md'))
            expected.extend(p.stem for p in paths[:count])
            for p in paths[count:]:
                state = history / category / p.name
                state.parent.mkdir(parents=True, exist_ok=True)
                state.touch()
                # Future timestamps clamp to age zero and the maximum penalty.
                os.utime(state, (4102444800, 4102444800))
        actual = self.picks(self.run_pick('--print', '--cooldown-dir', str(history)))
        self.assertEqual(set(actual), set(expected))

    def test_missing_or_insufficient_catalog_fails_before_output(self):
        category = self.skill / 'methods/operators'
        shutil.rmtree(category)
        result = self.run_pick('--seed', '42')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        category.mkdir()
        (category / 'only.md').write_text('# One method\n')
        result = self.run_pick('--seed', '42')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')

    def test_excludes_metadata_and_supports_nested_methods(self):
        category = self.skill / 'methods/operators'
        shutil.rmtree(category)
        (category / 'nested').mkdir(parents=True)
        for path in ['README.md', '_notes.md', 'nested/first.md', 'second.md']:
            (category / path).write_text('# Example\n')
        result = self.run_pick('--seed', '42', '--print')
        self.assertEqual(set(self.picks(result)[:2]), {'first', 'second'})

    def test_bodies_match_selected_methods(self):
        result = self.run_pick('--seed', '42')
        picks = self.picks(result)
        paths = re.findall(r'^----- (.+) -----$', result.stdout, re.M)
        self.assertEqual([Path(p).stem for p in paths], picks)
        for path in paths:
            self.assertIn(Path(path).read_text(), result.stdout)
        self.assertNotIn('----- /', self.run_pick('--seed', '42', '--print').stdout)

    def test_large_catalog_does_not_break_pipefail(self):
        category = self.skill / 'methods/operators'
        for i in range(600):
            (category / f'extra-{i}.md').write_text('# Extra\n')
        self.assertEqual(len(self.picks(self.run_pick('--seed', '42', '--print'))), 6)

    def test_standalone_rich_matches_plain(self):
        rich = self.root / 'rich only'
        shutil.copytree(REPO / 'ideonomy-rich', rich)
        self.assertEqual(self.run_pick('--seed', '42', '--print').stdout,
                         self.run_pick('--seed', '42', '--print', skill=rich).stdout)

    def test_shared_resources_are_in_sync(self):
        for folder in ['bin', 'methods', 'references']:
            left = REPO / 'ideonomy-plain' / folder
            right = REPO / 'ideonomy-rich' / folder
            def contents(root):
                return {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(contents(left), contents(right))

    def test_help(self):
        result = self.run_pick('--help')
        self.assertEqual(result.returncode, 0)
        self.assertIn('--cooldown-dir', result.stdout)


if __name__ == '__main__':
    unittest.main()
