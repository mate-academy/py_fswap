"""
docstring
"""


def fswap(filename1: str, filename2: str) -> None:
    """

    :param filename1:
    :param filename2:
    :return:
    """
    with open(filename1, 'r') as file1:
        lines = file1.readline()
        with open(filename2, 'w') as file2:
            for ind, line in enumerate(file1):
                if ind % 2 == 0:
                    file2.write(line)
                    continue
                file2.write(lines)
                lines = line
            file2.write(lines)
