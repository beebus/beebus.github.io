"""Parses python files and uses the pytest library to determine if they are 'bad' python files... incorrectly formed, syntax, etc."""

from pytest import raises
from .. import parse_file


def test_reader_error():
    with raises(IOError):
        parse_file('wat')
