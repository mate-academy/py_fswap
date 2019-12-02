"""
Swap each next pair of lines in the file
"""


def fswap(filename1: str, filename2: str) -> None:
    """Swap"""
    with open(filename1, 'rt') as rfile:
        strg = rfile.read()

    lst = strg.split('\n')[:-1]
    for i in range(1, len(lst), 2):
        lst[i-1], lst[i] = lst[i], lst[i-1]

    with open(filename2, 'wt') as wfile:
        wfile.write('\n'.join(lst)+'\n')
