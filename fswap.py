"""Swap each next pair of lines in the file."""
import itertools


def fswap(filename1: str, filename2: str) -> list:
    """Write to a new file swapped content of another file"""
    with open(filename1, 'rt', encoding='utf-8') as first_file:
        content = first_file.readlines()
        even_indexes = [v for k, v in enumerate(content) if k % 2 == 0]
        odd_indexes = [v for k, v in enumerate(content) if k % 2 != 0]
        sorted_arr = [j for i in itertools.zip_longest(odd_indexes, even_indexes) for j in i if j]
    with open(filename2, 'wt', encoding='utf-8') as second_file:
        for _ in sorted_arr:
            second_file.write(_)
    return sorted_arr
