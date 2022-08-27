from os.path import dirname, join, realpath
from re import escape
from tempfile import TemporaryDirectory

import pytest

from starter.utils import io

CURR_DIR = dirname(realpath(__file__))


@pytest.mark.parametrize("data", [{}, {"x": 9, "y": None, "z": {"a": "test", "b": [1, 2, 3]}}])
def test_yaml(data):
    assert isinstance(data, dict)
    with TemporaryDirectory(dir=CURR_DIR) as staging_dir:
        assert io.read_yaml(io.dump_yaml(data, join(staging_dir, "test.yaml"))) == data


def test_yaml_validation():
    with pytest.raises(FileNotFoundError, match=escape("No such file")):
        io.read_yaml("x")


if __name__ == "__main__":
    test_yaml()
