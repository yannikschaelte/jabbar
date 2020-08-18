"""The progress bar."""

import sys
from collections.abc import Iterable, Sized
from typing import TextIO, Tuple, Union
from unicodedata import east_asian_width as eaw

BAR_SYMBOLS = ('', '▏', '▎', '▍', '▌', '▋', '▊', '▉', '█')
BAR_PREFIX = ' |'
BAR_SUFFIX = '| '


class JabBar:
    """Just Another Beautiful progress BAR."""

    def __init__(
            self,
            iterable: Iterable = None,
            total: int = None,
            comment: str = "",
            width: int = 24,
            file: TextIO = sys.stdout,
            enable: bool = True,
            keep: bool = True,
            bar_symbols: Union[Tuple[str], str] = BAR_SYMBOLS):
        """Initialize the bar.

        :param iterable: An iterable to show the progress for while iterating
        :param total: The expected number of items
        :param comment: A comment to append to each line
        :param width: The width of the progress bar in characters
        :param file: The target where to write the progress bar to
        :param enable: Whether to actually show the progress bar
        :param keep: Whether to keep or remove the bar afterwards
        :param bar_symbols: Bar symbols to use, with increasing fill degree.
        """
        self.iterable = iterable
        self.total: int = total
        self.comment: str = comment
        self.width: int = width
        self.file: TextIO = file
        self.enable: bool = enable
        self.keep: bool = keep

        if isinstance(bar_symbols, str):
            bar_symbols = (bar_symbols,)
        bar_symbols = tuple(bar_symbols)
        if '' not in bar_symbols:
            # add empty element
            bar_symbols = ('',) + bar_symbols
        self.bar_symbols = bar_symbols

        self.n_done: int = 0
        self.len: int = 0

        if isinstance(iterable, Sized) and total is None:
            total = len(iterable)
        self.total = total

        if self.total is None:
            raise ValueError(
                "Either must the iterable have a length attribute, "
                "or a total been specified.")

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
        self.len = len(line)
        print(line, end=end, file=self.file)
        self.file.flush()

    def update(self, n_done: int) -> None:
        """Update the output.

        :param n_done: The number of finished tasks.
        """
        if not self.enable:
            return
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
        # number of full symbols
        n_symbol_full = int(n_full / nchar(self.bar_symbols[-1]))
        bar_full = self.bar_symbols[-1] * n_symbol_full

        # which of the bar symbols to select for the current symbol
        phase = int((width_full - n_full) * len(self.bar_symbols))
        # number of current symbols
        n_symbol_phase = 0
        if len(self.bar_symbols[phase]):
            n_symbol_phase = int(1 / nchar(self.bar_symbols[phase]))
        bar_current = self.bar_symbols[phase] * n_symbol_phase

        # number of empty symbols
        n_empty = self.width - nchar(bar_full) - nchar(bar_current)
        bar_empty = ' ' * n_empty

        str_done = f"{self.n_done}/{self.total}"

        line = ('\r' + str_r_done + BAR_PREFIX +
                bar_full + bar_current + bar_empty +
                BAR_SUFFIX + str_done +
                " " + self.comment)

        return line

    def inc(self, n: int = 1) -> None:
        """Update / increment by `n`.

        :param n: Number to increment by
        """
        self.update(self.n_done + n)

    def finish(self) -> None:
        """Finish the line by a line break."""
        if not self.enable:
            return
        if self.keep:
            self.write('', end='\n')
        else:
            self.write('\r' + ' ' * self.len + '\r')

    def __iter__(self):
        """Iterate over the iterable."""
        if self.iterable is None:
            raise ValueError(
                "To use jabbar in iterable mode, pass an iterable.")
        for val in self.iterable:
            yield val
            self.inc()
        self.finish()


def nchar(symbol: str) -> int:
    """Calculate number of unit-width characters for a symbol.

    This may not work on all systems and for all symbols.

    :param symbol: The symbol (single character or string).

    :returns: A guess of the number of unit-width characters.
    """
    return len(symbol) + sum(1 for char in symbol if eaw(char) in ['F', 'W'])


# convenience alias
jabbar = JabBar
