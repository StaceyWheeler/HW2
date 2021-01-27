import unittest
# import sys
# sys.path.insert(1, '/Users/stacey/Documents/DATA515/Newsgroup_repo/tests/newsgroup_analysis.py')
import newsgroup_analysis as nga


class EmailTest(unittest.TestCase):
    def test_read_in_all_files(self):
        nga.process_newsgroup_topic("test_FruitEmails/*")
        fruit_email_list = ['blueberry@fruit.abc', 'strawberry@fruit.abc', 'raspberry@fruit.abc']
        with open('sci.crypt.emails.txt') as f:
            for line in f:
                line = line.strip('\n')
                fruit_email_list.pop(fruit_email_list.index(line))
        self.assertNotEqual(len(fruit_email_list), 0, "All the files were read in")


if __name__ == '__main__':
    unittest.main()
