"""Test some basic routines of jabbar."""
import sys
import tempfile

from jabbar import jabbar

import pytest


def test_iter():
    """Test whether iter mode works."""
    for _ in jabbar(range(100)):
        pass


def test_manual():
    """Test whether manual setup mode works."""
    total = 50
    bar = jabbar(total=total)
    for _ in range(total):
        bar.inc()
    bar.finish()
    assert bar.n_done == total


def test_context():
    """Test whether context mode works."""
    total = 100
    with jabbar(total=total - 20) as bar:
        for _ in range(total):
            bar.inc()
        assert bar.n_done == total


def test_no_iterable():
    """Test failure when using iterable mode without iterable."""
    with pytest.raises(ValueError):
        for _ in jabbar(total=10):
            pass


def test_no_total():
    """Test failure when no total is available."""
    with pytest.raises(ValueError):
        jabbar()


def test_stderr():
    """Test output to stderr."""
    for _ in jabbar(range(100), file=sys.stderr):
        pass


def test_file():
    """Test output to file."""
    with tempfile.NamedTemporaryFile(mode='w+') as file:
        for _ in jabbar(range(100), file=file):
            pass


def test_enable():
    """Test enabling functionality."""
    for _ in jabbar(range(100), enable=False):
        pass


def test_keep():
    """Test the keep functionality."""
    for _ in jabbar(range(100), keep=False):
        pass


def test_custom_symbols():
    """Test passing custom bar symbols."""
    for _ in jabbar(range(100), bar_symbols='yo'):
        pass
