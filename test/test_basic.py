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
    with tempfile.NamedTemporaryFile(mode="w+") as file:
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
    for _ in jabbar(range(100), symbols="yo"):
        pass


def test_output():
    """Test the actual output."""
    total = 50
    bar = jabbar(total=total)
    for _ in range(20):
        bar.inc()
    out = bar.get_line()
    assert out == "\r 40% |█████████▋              | 20/50 "
    assert bar.n_done == 20
    bar.finish()


def test_output_custom_symbols():
    """Test the output with custom symbols."""
    total = 50
    bar = jabbar(total=total, symbols="xo")
    for _ in range(17):
        bar.inc()
    out = bar.get_line()
    assert out == "\r 34% |xoxoxoxo                | 17/50 "
    assert bar.n_done == 17
    bar.finish()
