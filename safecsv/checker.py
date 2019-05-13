import inspect
import re

class Checker:

    @classmethod
    def full_check(cls, stream, sep=',', quotechar=None, tests='all'):
        """Perform all the tests on the stream.

        Parameters
        ----------
        stream : file object
            An file-like object made of characters. It must suport call
            to the .seek() method.
        
        sep : char, optional
            The character to be considered as the columns separator.
            Default is , (comma).

        quotechar : char, optional
            The character to be considered as the text encloser.
            Default is " (quote).

        tests : {'core', 'extended', 'all'}, optional
            Sets the type of tests to be performed on the stream. It can
            either be 'core' to perform only the core tests, either
            'extended' for the extended tests or either 'all' for both
            the core and extended tests.
            Default is 'all'.
        """

        # find all the check_ methods in this class using introspection
        checks = list()
        if tests.lower() in ('all', 'core'):
            # find all the "core" tests
            checks += [x for x in inspect.getmembers(cls, inspect.isfunction) if x[0][:11] == 'check_core_']
        if tests.lower() in ('all', 'extended'):
            # find all the "extended" tests
            checks += [x for x in inspect.getmembers(cls, inspect.isfunction) if x[0][:11] == 'check_extd_']

        # display the name of the stream (if any)
        if hasattr(stream, 'name'):
            print('\033[34mStream: {name}\033[0m'.format(name=stream.name))

        # apply each check on the stream
        for check_name, check_fn in checks:

            # move the cursor at the begining of the stream
            stream.seek(0)

            # run the check on the stream
            success, err_line = check_fn(stream, sep, quotechar)

            if success:
                print('\033[32m{check_name} \u21E8 {check_desc}\033[0m'.format(
                    check_name=check_name, check_desc=check_fn.__doc__
                ))
            else:                
                print('\033[31m{check_name} \u21E8 flaw found at line {err_line}: {check_desc}\033[0m'.format(
                    check_name=check_name, err_line=err_line, check_desc=check_fn.__doc__
                ))
                return False  # abort testing
        
        # data are clean
        return True

    @staticmethod
    def check_core_01(stream, sep, quotechar):
        """Quotechar present in data must be escaped (doubled)"""

        if quotechar is None:
            # always True if the csv isn't escaped
            return [True, 0]

        cur_state = 0
        
        for i, line in enumerate(stream):

            line = line.strip('\r\n')

            for char in line:

                if cur_state == 0:
                    if char == quotechar:
                        cur_state = 2
                    elif char == sep:
                        pass
                    else:
                        cur_state = 1

                elif cur_state == 1:
                    if char == sep:
                        cur_state = 0
                    elif char == quotechar:
                        return [False, i+1] # syntax error
                    else:
                        pass

                elif cur_state == 2:
                    if char == quotechar:
                        cur_state = 3
                    else:
                        pass

                elif cur_state == 3:
                    if char == quotechar:
                        cur_state = 2
                    elif char == sep:
                        cur_state = 0
                    else:
                        return [False, i+1] # syntax error
                    
            # end of the line reached
            # equivalent of reaching \n character
            if cur_state != 2:
                cur_state = 0
        
        # end of the stream reached
        # equivalent of reaching EOF character
        if cur_state == 2:
            return [False, i+1] # syntax error
        else:
            return [True, 0]

    @staticmethod
    def check_core_02(stream, sep, quotechar):
        """Lines must have the same number of columns"""

        if quotechar is None:

            line = stream.readline()
            expected_nb_sep = line.count(sep)

            for i, line in enumerate(stream):

                nb_sep = line.count(sep)

                if nb_sep != expected_nb_sep:
                    return [False, i+2]

            return [True, 0]
            
        else:

            line = stream.readline()
            expected_nb_sep = line.count(sep)
            cur_line_nb_sep = 0

            cur_state = 0

            for i, line in enumerate(stream):

                line = line.strip('\r\n')

                for char in line:

                    if cur_state == 0:
                        if char == quotechar:
                            cur_state = 2
                        elif char == sep:
                            cur_line_nb_sep += 1
                        else:
                            cur_state = 1

                    elif cur_state == 1:
                        if char == sep:
                            cur_state = 0
                            cur_line_nb_sep += 1
                        elif char == quotechar:
                            return [False, i+1] # syntax error
                        else:
                            pass

                    elif cur_state == 2:
                        if char == quotechar:
                            cur_state = 3
                        else:
                            pass

                    elif cur_state == 3:
                        if char == quotechar:
                            cur_state = 2
                        elif char == sep:
                            cur_state = 0
                            cur_line_nb_sep += 1
                        else:
                            return [False, i+2] # syntax error
                        
                # end of the line reached
                # equivalent of reaching \n character
                if cur_state != 2:
                    cur_state = 0
                    if cur_line_nb_sep != expected_nb_sep:
                        return [False, i+2] # wrong number of columns
                    cur_line_nb_sep = 0
            
            # end of the stream reached
            # equivalent of reaching EOF character
            if cur_state == 2:
                return [False, i+2] # syntax error
            else:
                return [True, 0]

            return [True, 0]

    @staticmethod
    def check_extd_01(stream, sep, quotechar):
        """Header must contain only letters, numbers or underscores"""

        # retrieve the header
        header = stream.readline()

        # remove sep, quotechar and trailing newline
        header = header.rstrip('\r\n').replace(sep, '')
        if quotechar is not None:
            header = header.replace(quotechar, '')

        # search for forbidden characters
        if re.search('[^a-zA-Z0-9_]', header):
            return [False, 0]

        return [True, 0]
