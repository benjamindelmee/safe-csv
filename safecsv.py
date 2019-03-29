import inspect
import re

class Check:

    @classmethod
    def full_check(cls, filename, sep=',', delimiter=None):

        # find all the check_ methods in this class using introspection
        checks = [x for x in inspect.getmembers(cls, inspect.isfunction) if x[0][:6] == 'check_']

        # apply each check on the file
        for check_name, check_fn in checks:

            # open the file and run the check
            with open(filename, 'r') as f:
                success, err_line = check_fn(f, '', '')

            if success:
                print('\033[32m{check_name} \u21E8  everything is fine \033[0m'.format(check_name=check_name))
            else:                
                print('\033[31m{check_name} \u21E8  flaw found at line {err_line}: {check_desc}\033[0m'.format(
                    check_name=check_name, err_line=err_line, check_desc=check_fn.__doc__)
                )
                return False  # abort testing
        
        # data are clean
        return True

    @staticmethod
    def check_01(file, sep, delimiter):
        """test"""

        return [True, 0]

    @staticmethod
    def check_02(file, sep, delimiter):
        """test"""

        return [True, 0]

    @staticmethod
    def check_03(file, sep, delimiter):
        """test"""

        return [False, 0]

Check.full_check('./data/test.csv')