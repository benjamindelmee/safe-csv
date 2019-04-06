import unittest
import inspect
from safecsv import Checker

class Test(unittest.TestCase):

    valid_files = {
        'path': './data/valid_files',
        'files': [
            # normal CSV without eccentricity
            {'filename': 'valid_01_comma.csv', 'sep': ',', 'quotechar': None},
            {'filename': 'valid_01_comma_with_quote.csv', 'sep': ',', 'quotechar': '"'},
            {'filename': 'valid_01_tab.csv', 'sep': '\t', 'quotechar': None},

            # CSV with only one column
            {'filename': 'valid_02.csv', 'sep': ',' , 'quotechar': None},
            {'filename': 'valid_02_with_quote.csv', 'sep': ',' , 'quotechar': '"'},

            # CSV without data, only header
            {'filename': 'valid_03_comma.csv', 'sep': ',', 'quotechar': None},
            {'filename': 'valid_03_comma_with_quote.csv', 'sep': ',', 'quotechar': '"'},
            {'filename': 'valid_03_tab.csv', 'sep': '\t', 'quotechar': None},
            
            # CSV with empty fields
            {'filename': 'valid_04_comma.csv', 'sep': ',' , 'quotechar': None},
            {'filename': 'valid_04_comma_with_quote.csv', 'sep': ',' , 'quotechar': '"'},
            {'filename': 'valid_04_tab.csv', 'sep': '\t', 'quotechar': None},

            # CSV with separator inside quoted fields
            {'filename': 'valid_05_comma_with_quote.csv', 'sep': ',' , 'quotechar': '"'},
            {'filename': 'valid_05_tab_with_quote.csv', 'sep': '\t', 'quotechar': '"'},

            # CSV with escaped quote inside quoted fields
            {'filename': 'valid_06_comma_with_quote.csv', 'sep': ',' , 'quotechar': '"'},
            {'filename': 'valid_06_tab_with_quote.csv', 'sep': '\t', 'quotechar': '"'},
        ]
    }
    
    #
    # Tests commun to all check_ methods
    #

    def test_check_valid_files(self):
        """Test if check_ methods return True for valid files"""

        # find all the check_ methods in the Checker class using introspection
        checks = [x for x in inspect.getmembers(Checker, inspect.isfunction) if x[0][:6] == 'check_']

        # iterate over each check_ methods
        for f_name, func in checks:

            # iterate over each valid file
            for valid_file in self.valid_files['files']:

                filepath = self.valid_files['path'] + '/' + valid_file['filename']

                # open the file to test
                with open(filepath, 'r') as file_to_test:

                    # create a subtest for this set of parameters
                    with self.subTest(check=f_name, filename=valid_file['filename']):
                        sep = valid_file['sep']
                        quotechar = valid_file['quotechar']

                        # run the test
                        res = func(file_to_test, sep=sep, quotechar=quotechar)[0]

                        # assert the result
                        self.assertEqual(res, True)

    #
    # Tests on method check_01
    #
    
    def test_check_01_T01(self):
        with open('./data/check_01/check_01_T01.csv', 'r') as f:
            res = Checker.check_01(f, sep=',', quotechar=None)[0]
            self.assertEqual(res, False)

    def test_check_01_T01_tab(self):
        with open('./data/check_01/check_01_T01_tab.csv', 'r') as f:
            res = Checker.check_01(f, sep='\t', quotechar=None)[0]
            self.assertEqual(res, False)

    def test_check_01_T02(self):
        with open('./data/check_01/check_01_T02.csv', 'r') as f:
            res = Checker.check_01(f, sep=',', quotechar=None)[0]
            self.assertEqual(res, False)

    def test_check_01_T02_tab(self):
        with open('./data/check_01/check_01_T02_tab.csv', 'r') as f:
            res = Checker.check_01(f, sep='\t', quotechar=None)[0]
            self.assertEqual(res, False)

    def test_check_01_T03(self):
        with open('./data/check_01/check_01_T03.csv', 'r') as f:
            res = Checker.check_01(f, sep=',', quotechar=None)[0]
            self.assertEqual(res, False)
    
    def test_check_01_T03_tab(self):
        with open('./data/check_01/check_01_T03_tab.csv', 'r') as f:
            res = Checker.check_01(f, sep='\t', quotechar=None)[0]
            self.assertEqual(res, False)

    #
    # Tests on method check_02
    #
    
    def test_check_02_T01(self):
        with open('./data/check_02/check_02_T01.csv', 'r') as f:
            res = Checker.check_02(f, sep=',', quotechar='"')
            self.assertEqual(res, [False, 2])
    
    def test_check_02_T01_tab(self):
        with open('./data/check_02/check_02_T01_tab.csv', 'r') as f:
            res = Checker.check_02(f, sep='\t', quotechar='"')
            self.assertEqual(res, [False, 2])
    
    def test_check_02_T02(self):
        with open('./data/check_02/check_02_T02.csv', 'r') as f:
            res = Checker.check_02(f, sep=',', quotechar='"')
            self.assertEqual(res, [False, 2])
    
    def test_check_02_T02_tab(self):
        with open('./data/check_02/check_02_T02_tab.csv', 'r') as f:
            res = Checker.check_02(f, sep='\t', quotechar='"')
            self.assertEqual(res, [False, 2])
    
    def test_check_02_T03(self):
        with open('./data/check_02/check_02_T03.csv', 'r') as f:
            res = Checker.check_02(f, sep=',', quotechar='"')
            self.assertEqual(res, [False, 2])
    
    def test_check_02_T03_tab(self):
        with open('./data/check_02/check_02_T03_tab.csv', 'r') as f:
            res = Checker.check_02(f, sep='\t', quotechar='"')
            self.assertEqual(res, [False, 2])

    def test_check_02_T04(self):
        with open('./data/check_02/check_02_T04.csv', 'r') as f:
            res = Checker.check_02(f, sep=',', quotechar='"')
            self.assertEqual(res, [True, 0])
    
    def test_check_02_T04_tab(self):
        with open('./data/check_02/check_02_T04_tab.csv', 'r') as f:
            res = Checker.check_02(f, sep='\t', quotechar='"')
            self.assertEqual(res, [True, 0])
    
    def test_check_02_T05(self):
        with open('./data/check_02/check_02_T05.csv', 'r') as f:
            res = Checker.check_02(f, sep=',', quotechar='"')
            self.assertEqual(res, [False, 2])

    def test_check_02_T05_tab(self):
        with open('./data/check_02/check_02_T05_tab.csv', 'r') as f:
            res = Checker.check_02(f, sep='\t', quotechar='"')
            self.assertEqual(res, [False, 2])

    #
    # Tests on method check_03
    #
    
    def test_check_03_T01(self):
        with open('./data/check_03/check_03_T01.csv', 'r') as f:
            res = Checker.check_03(f, sep=',', quotechar=None)
            self.assertEqual(res, [False, 3])

    def test_check_03_T01_tab(self):
        with open('./data/check_03/check_03_T01_tab.csv', 'r') as f:
            res = Checker.check_03(f, sep='\t', quotechar=None)
            self.assertEqual(res, [False, 3])
    
    def test_check_03_T02(self):
        with open('./data/check_03/check_03_T02.csv', 'r') as f:
            res = Checker.check_03(f, sep=',', quotechar=None)
            self.assertEqual(res, [False, 3])
    
    def test_check_03_T02_tab(self):
        with open('./data/check_03/check_03_T02_tab.csv', 'r') as f:
            res = Checker.check_03(f, sep='\t', quotechar=None)
            self.assertEqual(res, [False, 3])

if __name__ == '__main__':
    unittest.main()