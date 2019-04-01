def update_pypath():
    """add safecsv to the python import path"""
    import sys, os
    # find the absolute path of the test directory
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    # add the above directory to the python path
    sys.path.append('{}/..'.format(cur_dir))
    # import our custom library
    
update_pypath()

import unittest
import inspect
from safecsv.checker import Checker

class Test(unittest.TestCase):

    valid_files = {
        'path': './data/valid_files',
        'files': [
            {'filename': 'valid_01_comma.csv', 'sep': ',', 'delimiter': None},
            {'filename': 'valid_01_comma_with_quote.csv', 'sep': ',', 'delimiter': '"'},
            {'filename': 'valid_01_tab.csv', 'sep': '\t', 'delimiter': None},

            {'filename': 'valid_02.csv', 'sep': ',' , 'delimiter': None},
            {'filename': 'valid_02_with_quote.csv', 'sep': ',' , 'delimiter': None},

            {'filename': 'valid_03_comma.csv', 'sep': ',', 'delimiter': None},
            {'filename': 'valid_03_comma_with_quote.csv', 'sep': ',', 'delimiter': '"'},
            {'filename': 'valid_03_tab.csv', 'sep': '\t', 'delimiter': None},
            
            {'filename': 'valid_04_comma.csv', 'sep': ',' , 'delimiter': None},
            {'filename': 'valid_04_comma_with_quote.csv', 'sep': ',' , 'delimiter': '"'},
            {'filename': 'valid_04_tab.csv', 'sep': '\t', 'delimiter': None},
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
                        delimiter = valid_file['delimiter']

                        # run the test
                        res = func(file_to_test, sep=sep, delimiter=delimiter)[0]

                        # assert the result
                        self.assertEqual(res, True)

    #
    # Tests on method check_01
    #
    
    def test_check_01_T01(self):
        pass # TODO

    def test_check_01_T02(self):
        pass # TODO

    #
    # Tests on method check_02
    #
    
    def test_check_02_T01(self):
        pass # TODO

    def test_check_02_T02(self):
        pass # TODO

if __name__ == '__main__':
    unittest.main()