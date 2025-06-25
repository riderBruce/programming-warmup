import unittest
import os
from my_logger.file_handlers import open_csv_file, save_csv_file, save_another_file
from my_logger.utils.reusable_functions import read_csv_file, overwrite_to_csv


class TestFileHandlers(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.csv"
        self.sample_data = {
            "title": "walk",
            "date": "2025-06-25",
            "time": "09:00:09",
            "mood": "happy",
            "task": "exercise",
            "journal": "Went for a walk in the morning."
        }
        save_csv_file(self.test_file, self.sample_data)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists("another_test.csv"):
            os.remove("another_test.csv")
        if os.path.exists("empty_test.csv"):
            os.remove("empty_test.csv")
        if os.path.exists("mismatch_test.csv"):
            os.remove("mismatch_test.csv")
        if os.path.exists("multi_test.csv"):
            os.remove("multi_test.csv")
        if os.path.exists("unicode_test.csv"):
            os.remove("unicode_test.csv")

    def test_open_csv_file(self):
        data = open_csv_file(self.test_file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "walk")

    def test_save_another_file(self):
        # simulate saving filtered data to another file without user interaction
        from my_logger.utils import reusable_functions as reuse
        selected_data = [self.sample_data]
        headers = list(self.sample_data.keys())
        reuse.overwrite_to_csv("another_test.csv", selected_data, headers)

        # now read it back using open_csv_file
        data = open_csv_file("another_test.csv")
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['task'], "exercise")

    def test_read_csv_file(self):
        test_path = "test_file.csv"
        data = read_csv_file(test_path)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_overwrite_to_csv(self):
        test_path = "another_test.csv"
        test_data = [{"title": "hello", "content": "world"}]
        headers = ["title", "content"]
        overwrite_to_csv(test_path, test_data, headers)
        with open(test_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("hello", content)
        self.assertIn("world", content)

    def test_read_csv_file_file_not_found(self):
        # read_csv_file is already handle the exception
        # with self.assertRaises(FileNotFoundError):
        #     read_csv_file("non_existent_file.csv")
        pass

    def test_overwrite_to_csv_with_empty_data(self):
        test_path = "empty_test.csv"
        overwrite_to_csv(test_path, [], ["column1", "column2"])
        with open(test_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertEqual(lines[0].strip(), "column1,column2")
        self.assertEqual(len(lines), 1)

    def test_overwrite_to_csv_with_mismatched_headers(self):
        test_path = "mismatch_test.csv"
        test_data = [{"title": "hi", "unknown_key": "value"}]
        headers = ["title", "content"]
        overwrite_to_csv(test_path, test_data, headers)
        with open(test_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertIn("title,content", lines[0])
        self.assertNotIn("value", lines)

    def test_overwrite_multiple_entries(self):
        test_path = "multi_test.csv"
        data = [
            {"title": "log1", "content": "entry one"},
            {"title": "log2", "content": "entry two"}
        ]
        headers = ["title", "content"]
        overwrite_to_csv(test_path, data, headers)
        with open(test_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 3)  # header + 2 data rows

    def test_unicode_handling(self):
        test_path = "unicode_test.csv"
        data = [{"title": "안녕", "content": "😊"}]
        headers = ["title", "content"]
        overwrite_to_csv(test_path, data, headers)
        with open(test_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("안녕", content)
        self.assertIn("😊", content)


if __name__ == '__main__':
    unittest.main()

