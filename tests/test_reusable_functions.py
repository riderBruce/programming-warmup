import unittest
import os
import csv
from my_logger.utils import reusable_functions as reuse


class TestReusableFunctions(unittest.TestCase):

    def setUp(self):
        # This runs before every test
        self.test_file = "test_log.csv"
        self.sample_data = {
            "title": "test",
            "date": "2025-06-24",
            "time": "14:33:00",
            "mood": "neutral",
            "task": "coding",
            "journal": "Just testing"
        }
        # Write header and first row
        reuse.add_dict_to_csv(self.test_file, self.sample_data)

    def tearDown(self):
        # This runs after every test - clean up
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_is_valid_datetime(self):
        self.assertTrue(reuse.is_valid_datetime('2025-06-20', '%Y-%m-%d'))
        self.assertTrue(reuse.is_valid_datetime('14:30:20', '%H:%M:%S'))
        self.assertFalse(reuse.is_valid_datetime('25-06-2025', '%Y-%m-%d'))
        self.assertFalse(reuse.is_valid_datetime('143020', '%H:%M:%S'))

    def test_add_dict_to_csv_and_read_csv_file(self):
        # Read it back in
        entries = reuse.read_csv_file(self.test_file)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["title"], "test")
        self.assertEqual(entries[0].keys(), self.sample_data.keys())

    def test_select_yes_or_no_simulated(self):
        # Normally this uses input(), so we won't test it here
        pass

    def test_overwrite_to_csv(self):
        entries_before = [self.sample_data, self.sample_data, self.sample_data]
        reuse.overwrite_to_csv(self.test_file, entries_before, list(self.sample_data.keys()))
        entries = reuse.read_csv_file(self.test_file)
        self.assertEqual(len(entries), 3)
        self.assertEqual(entries[1]['task'], "coding")
        self.assertEqual(entries[2].keys(), self.sample_data.keys())


if __name__ == '__main__':
    unittest.main()
