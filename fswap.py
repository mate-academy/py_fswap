"""
module file swap
"""
from typing import List, Any


def pairwise_swap(lst: List[Any]) -> List[Any]:
    """
    Pairwise swapping in list.
    :param lst: List[Any]
    :return: List[Any]
    """
    length = len(lst)
    # stop at second last if length is odd, otherwise use full list.
    end = length - 1 if length % 2 else length
    lst[1:end:2], lst[:end:2] = lst[:end:2], lst[1:end:2]
    return lst


def fswap(filename1: str, filename2: str) -> None:
    """
    Swap each next pair of lines in the file.
    :param filename1: str
    :param filename2: str
    :return: None
    """
    with open(filename1, 'rt') as file_1:
        with open(filename2, 'wt') as file_2:
            lines_lst = file_1.readlines()
            for line in pairwise_swap(lines_lst):
                file_2.write(line)
