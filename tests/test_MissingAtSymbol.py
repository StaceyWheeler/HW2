import unittest
# import sys
# sys.path.insert(1, '/Users/stacey/Documents/DATA515/Newsgroup_repo/tests/newsgroup_analysis.py')
import newsgroup_analysis as nga

class EmailTest(unittest.TestCase):
    def test_missing_at(self):
        missing_at_symbol = 'personal.domain.com'
        self.assertFalse(nga.check_email_validity(missing_at_symbol), "This is missing the @ symbol")

    def test_double_at(self):
        double_at_symbol = 'personal@domain@com'
        self.assertFalse(nga.check_email_validity(double_at_symbol), "This is missing the @ symbol")

if __name__ == '__main__':
    unittest.main()