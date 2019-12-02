'''
Module
'''


def fswap(read_file: str, write_file: str) -> None:
    '''
    Swap each next pair of lines in the file.
    :param read_file:
    :param write_file:
    :return:
    '''
    with open(read_file, "rt") as reading:
        with open(write_file, "wt") as writing:
            flag, remember_line = True, ''
            for line in reading:
                if flag:
                    remember_line = line
                    flag = False
                else:
                    writing.write(line)
                    writing.write(remember_line)
                    flag = True
            if not flag:
                writing.write(remember_line)
