"""This code copies contents from one file to another
and changes each 2 lines order"""


def fswap(filename1: str, filename2: str) -> None:
    """
    Copy the file on line-by-line basis in pair-swapped order
    :param filename1: original file, the source for copying
    :param filename2: new file, the destination for copying
    :return: none as the result is new contents of the second file
    """
    to_be_copied = []
    with open("%s" % filename1, "rt") as func:
        for line in func:
            to_be_copied.append(line)
    for item in range(0, len(to_be_copied), 2):
        try:
            to_be_copied[item], to_be_copied[item + 1] = to_be_copied[item + 1], to_be_copied[item]
        except IndexError:
            pass
    with open("%s" % filename2, "wt") as func:
        func.writelines(to_be_copied)
