import os
import pytest
import fswap


@pytest.fixture
def files():
    old_file = "test1"
    new_file = "test2"
    with open(old_file, "wt") as f:
        f.write("1\n2\n3\n4\n5\n")
    yield old_file, new_file
    os.remove(old_file)
    os.remove(new_file)


def test_fswap(files):
    fswap.fswap(*files)
    with open(files[1], "rt") as f:
        assert f.read() == "2\n1\n4\n3\n5\n"