"""docstring"""


def fswap(filename1: str, filename2: str) -> None:
    """swap element"""

    file_read = open(filename1)
    file_write = open(filename2, 'w')
    list_item = file_read.readlines()
    if len(list_item) % 2:
        end = len(list_item) - 1
    else:
        end = len(list_item)
    list_item[1:end:2], list_item[:end:2] = list_item[:end:2], list_item[1:end:2]
    for i in list_item:
        file_write.write(i)

    file_read.close()
    file_write.close()
