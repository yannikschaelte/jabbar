"""The progress bar."""

import sys
from collections.abc import Iterable, Sized
from typing import TextIO

bar_symbols = ('', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█')
bar_prefix = ' |'
bar_suffix = '| '


class JabBar:
    """Just Another Beautiful progress BAR."""

    def __init__(
            self,
            iterable: Iterable = None,
            total: int = None,
            width: int = 24,
            file: TextIO = sys.stdout):
        """Initialize the bar.

        :param iterable: An iterable to show the progress for while iterating
        :param total: The expected number of items
        :param width: The width of the progress bar in characters
        :param file: The target where to write the progress bar to.
        """
        self.iterable = iterable
        self.total: int = total
        self.width: int = width
        self.file: TextIO = file
        self.n_done: int = 0

        if isinstance(iterable, Sized) and total is None:
            total = len(iterable)
        self.total = total

        if self.total is None:
            raise ValueError(
                "Either the iterable must have a length attribute, "
                "or a total must have been specified.")

    def __enter__(self):
        """Prepare upon entering a context manager."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Tidy up Upon exiting a context manager."""
        self.finish()

    def write(self, line: str, end='') -> None:
        """Write a line.

        :param line: The line to write, will be prefixed by a carriage return
        :param end: Symbol for the end of the line
        """
        """Write a line in-place."""
        print('\r' + line, end=end, file=self.file)

    def update(self, n_done: int) -> None:
        """Update the output.

        :param n_done: The number of finished tasks.
        """
        self.n_done = n_done
        line = self.get_line()
        self.write(line)

    def get_line(self) -> str:
        """Create the line containing the progress bar.

        :returns line: The line
        """
        # fraction of done vs total
        r_done = self.n_done / self.total
        str_r_done = f"{int(r_done * 100):3}%"

        # width of the filled bar
        width_full = self.width * min(r_done, 1)

        # number of full bar fields is the integer below
        n_full = int(width_full)
        bar_full = bar_symbols[-1] * n_full

        # which of the bar symbols to select
        phase = int((width_full - n_full) * len(bar_symbols))
        bar_current = bar_symbols[phase]

        n_empty = self.width - n_full - len(bar_current)
        bar_empty = ' ' * n_empty

        str_done = f"{self.n_done}/{self.total}"

        line = (str_r_done + bar_prefix +
                bar_full + bar_current + bar_empty +
                bar_suffix + str_done)

        return line

    def inc(self, n: int = 1) -> None:
        """Update / increment by `n`.

        :param n: Number to increment by
        """
        self.update(self.n_done + n)

    def finish(self) -> None:
        """Finish the line by a line break."""
        self.write('', end='\n')

    def __iter__(self):
        """Iterate over the iterable."""
        if self.iterable is None:
            raise ValueError("")
        for val in self.iterable:
            yield val
            self.inc()
        self.finish()


# convenience alias
jabbar = JabBar
