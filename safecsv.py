import inspect

class Check:

    @classmethod
    def full_check(cls, filename, sep=',', delimiter=None):

        # find all the check_ methods in this class using introspection
        checks = [x for x in inspect.getmembers(cls, inspect.ismethod) if x[0][:6] == 'check_']

        # apply each check on the file
        for check, function in checks:

            # open the file and run the check
            with open(filename, 'r') as f:
                success, err, err_line = function(f, '', '')

            if success:
                print('\033[32m{check} \u21E8  everything is fine \033[0m'.format(check=check))
            else:                
                print('\033[31m{check} \u21E8  flaw found at line {line}: {desc}\033[0m'.format(check=check, line=err_line, desc=err))
                return False  # abort testing
        
        # data are clean
        return True

    @classmethod
    def check_01(cls, file, sep, delimiteur):
        return [True, '', 0]

    @classmethod
    def check_02(cls, file, sep, delimiteur):
        return [True, '', 0]
    
    @classmethod
    def check_03(cls, file, sep, delimiteur):
        return [False, 'Blablabla', 0]

Check.full_check('./data/test.csv')