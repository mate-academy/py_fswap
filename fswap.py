"""
Swap each next pair of lines in the file.
"""


def fswap(filename1: str, filename2: str) -> None:
    """Swap each next pair of lines in the file."""
    result = ['']
    with open(filename1, 'rt') as reader:
        result = reader.readlines()
        for index, _val in enumerate(result):
            if index % 2:
                continue
            try:
                result[index], result[index+1] = result[index+1], result[index]
            except IndexError:
                break
    with open(filename2, 'w') as writer:
        writer.write(''.join(result))
