import unittest
from unittest.mock import patch
from my_logger.log_actions import (
    add_data_in_memory,
    write_log,
    view_recent_logs,
    search_logs_by_keyword,
    search_tasks_by_date,
    search_key,
    search_date
)

# Sample log entry
sample_entry = {
    "title": "coding",
    "date": "2025-06-25",
    "time": "10:00:00",
    "mood": "focused",
    "task": "project",
    "journal": "Worked on the logger CLI."
}


class TestLogActions(unittest.TestCase):

    def setUp(self):
        self.data = []

    def test_add_data_in_memory(self):
        add_data_in_memory(self.data, sample_entry)
        self.assertEqual(len(self.data), 1)
        self.assertEqual(self.data[0]['title'], "coding")

    # @patch('builtins.input', side_effect=["test title", "happy", "study", "Refactored my logger."])
    # @patch('my_logger.log_actions.save_csv_file')
    # def test_write_log(self, mock_save, mock_input):
    #     # Assumes get_log_input is using input() directly
    #     data = []
    #     write_log(data, "log.csv")
    #     self.assertEqual(len(data), 1)
    #     mock_save.assert_called_once()

    def test_search_key(self):
        self.data.append(sample_entry)
        key = 'the'
        results = search_key(self.data, key)
        # self.assertIn(key, ''.join(results[0].values()))
        self.assertTrue(any(key in v for v in results[0].values()))
        self.assertNotIn('GUI', results)

    def test_search_date(self):
        self.data.append(sample_entry)
        date = '2025-06-25'
        results = search_date(self.data, date)
        self.assertIn(date, results[0].values())
        self.assertNotIn('2025-06-19', results)

    def test_search_key_no_match(self):
        self.data.append(sample_entry)
        results = search_key(self.data, "nonexistent")
        self.assertEqual(results, [])

    def test_search_key_none(self):
        self.data.append(sample_entry)
        results = search_key(self.data, None)
        self.assertTrue(len(results) == 0)

    def test_search_date_no_date(self):
        sample_entry.pop('date')
        self.data.append(sample_entry)
        date = '2025-06-25'
        results = search_date(self.data, date)
        self.assertEqual(results, [])

    def test_search_key_non_string_values(self):
        self.data.append({"title": 123, "mood": True})
        results = search_key(self.data, "1")
        self.assertEqual(results, [])

if __name__ == '__main__':
    unittest.main()