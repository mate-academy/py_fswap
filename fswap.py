"""swap module"""


def fswap(filename1: str, filename2: str) -> None:
    """
    swap every two line in file
    :param filename1: file for reading
    :param filename2: file for writing
    :return: None
    """
    with open(filename1, 'rt') as file_1:
        with open(filename2, 'wt') as file_2:
            attempt = 0
            for line in file_1:
                if not attempt % 2:
                    old_line = line
                else:
                    file_2.write(line)
                    file_2.write(old_line)
                attempt += 1
            if attempt % 2:
                file_2.write(old_line)
