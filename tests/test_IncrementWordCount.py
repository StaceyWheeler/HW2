import unittest
# import sys
# sys.path.insert(1, '/Users/stacey/Documents/DATA515/Newsgroup_repo/tests/newsgroup_analysis.py')
import newsgroup_analysis as nga


class EmailTest(unittest.TestCase):

    def test_increment_word_dict(self):
        file_path = 'tests/test_FruitEmails/blueberry_blueberry.txt'
        word_counts = {}
        nga.process_newsgroup_file(file_path, word_counts)
        self.assertEqual(word_counts['blueberry'], 2, "The word_count is not incrementing correctly")



if __name__ == '__main__':
    unittest.main()