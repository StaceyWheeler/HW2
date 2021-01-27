import unittest
# import sys
# sys.path.insert(1, '/Users/stacey/Documents/DATA515/Newsgroup_repo/tests/newsgroup_analysis.py')
import newsgroup_analysis as nga


class EmailTest(unittest.TestCase):

    def test_email_format_error(self):
        file_path = 'tests/text_file.txt'
        word_counts = {}
        self.assertRaises(nga.EmailFormatError, nga.process_newsgroup_file, file_path, word_counts)


if __name__ == '__main__':
    unittest.main()
