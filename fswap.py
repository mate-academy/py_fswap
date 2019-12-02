"""module docstring"""


def fswap(filename1: str, filename2: str) -> None:
    """read file1 line by line and write each pair of lines to file2 in swapped order """
    with open(filename1, "rt") as old_file:
        with open(filename2, "wt") as new_file:
            line_number = None
            for line_number, line in enumerate(old_file, 1):
                #  remember odd line
                if line_number % 2:
                    previous_line = line
                #  write even and previous line
                if not line_number % 2:
                    new_file.write(line)
                    new_file.write(previous_line)
            #  write last line if number of lines is odd
            if line_number % 2:
                new_file.write(previous_line)
