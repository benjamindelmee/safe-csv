import inspect
import re

class Checker:

    @classmethod
    def full_check(cls, filename, sep=',', delimiter=None):

        # find all the check_ methods in this class using introspection
        checks = [x for x in inspect.getmembers(cls, inspect.isfunction) if x[0][:6] == 'check_']

        # apply each check on the file
        for check_name, check_fn in checks:

            # open the file and run the check
            with open(filename, 'r') as f:
                success, err_line = check_fn(f, sep, delimiter)

            if success:
                print('\033[32m{check_name} \u21E8  {check_desc}\033[0m'.format(
                    check_name=check_name, check_desc=check_fn.__doc__
                ))
            else:                
                print('\033[31m{check_name} \u21E8  flaw found at line {err_line}: {check_desc}\033[0m'.format(
                    check_name=check_name, err_line=err_line, check_desc=check_fn.__doc__
                ))
                return False  # abort testing
        
        # data are clean
        return True

    @staticmethod
    def check_01(file, sep, delimiter):
        """Header must contain only letters, numbers or underscores"""

        # retrieve the header
        header = file.readline()

        # remove sep, delimiteur and trailing newline
        header = header.replace(sep, '').rstrip()
        if delimiter is not None:
            header = header.replace(delimiter, '')

        # search for forbidden characters
        if re.search('[^a-zA-Z0-9_]', header):
            return [False, 0]

        return [True, 0]

    @staticmethod
    def check_02(file, sep, delimiter):
        """Lines must contain only printable characters"""

        # apply the test on each line
        for i, line in enumerate(file):

            # remove trailing newlines
            line = line.rstrip()

            # remove tabs if they are used as separator
            if '\n' in sep:
                line = line.replace('\n', '')

            # search for non printable characters
            if not line.isprintable():
                return [False, i+1]

        return [True, 0]

    # TODO: implements these tests and their unittest:
    # text delimiteurs present in text must be escaped
    # each line must have the same amount of columns
    