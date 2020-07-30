"""Test some basic routines of jabbar."""

from jabbar import JabBar


def test_iter():
    """Test whether iter mode works."""
    for _ in JabBar(range(100)):
        pass


def test_manual():
    """Test whether manual setup mode works."""
    total = 50
    bar = JabBar(total=total)
    for _ in range(total):
        bar.inc()
    bar.finish()
    assert bar.n_done == total


def test_context():
    """Test whether context mode works."""
    total = 100
    with JabBar(total=total - 20) as bar:
        for _ in range(total):
            bar.inc()
        assert bar.n_done == total
