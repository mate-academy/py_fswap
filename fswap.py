"""
fswap module
Functions:
    fswap(filename1, filename2) -- swap each next
pair of lines in file filename1 and write it
to the file filename2.
"""


def fswap(filename1: str, filename2: str) -> None:
    """
    Read content of the file filename1, swap each next
pair of lines in the content, write result
to the filename2
    :param filename1: str
    :param filename2: str
    :return: None
    """
    with open(filename1, 'r') as file:
        context = file.read()

    num_of_lines = context.count('\n')
    if num_of_lines % 2:
        lines = context.split('\n', num_of_lines - 1)
    else:
        lines = context.split('\n')

    for idx in range(1, len(lines), 2):
        lines[idx], lines[idx - 1] = lines[idx - 1], lines[idx]
    swapped = '\n'.join(lines)

    with open(filename2, 'w') as file:
        file.write(swapped)
