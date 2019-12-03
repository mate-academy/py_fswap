"""docstring"""


def fswap(filename1: str, filename2: str) -> None:
    """swap element"""
    with open(filename1, 'rt') as file_read:
        with open(filename2, 'wt') as file_write:
            list_item = file_read.readlines()
            if len(list_item) % 2:
                end = len(list_item) - 1
            else:
                end = len(list_item)
            list_item[1:end:2], list_item[:end:2] = list_item[:end:2], list_item[1:end:2]
            for i in list_item:
                file_write.write(i)
