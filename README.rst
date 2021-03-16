jabbar
======

|build| |coverage| |pypi|

Just Another Beautiful progress BAR (some might replace Beautiful by Boring).

jabbar is a python package implementing a simple progress bar. The output
looks like:

.. code-block:: sh

   75% |█████████████████      | 750/1000

It is lightweight, easy to use and customizable.
As a special feature, it gracefully deals with seeing more items than expected, e.g. 1100/1000.
Also, it supports unicorns.

|shell|

For very serious work, you may want to try e.g. the slightly more professional `tqdm <https://github.com/tqdm/tqdm>`_ package.


Install
-------

jabbar can be installed from `PyPI <https://pypi.org/project/jabbar>`_ via your favorite shell:

.. code-block:: sh

   $ pip install jabbar

or from the latest code on `GitHub <https://github.com/yannikschaelte/jabbar>`_ with:

.. code-block:: sh

   $ pip install git+https://github.com/yannikschaelte/jabbar.git


Get started
-----------

jabbar is quite flexible and can operate in different modes.

jabbar can simply wrap around any iterable to make loops show a little progress
bar:

.. code-block:: python

   from jabbar import jabbar
   for _ in jabbar(range(1000)):
       pass

The updating scheme can also be individually specified:

.. code-block:: python

   from jabbar import jabbar
   with jabbar(total=1000, width=30) as bar:
       for _ in range(50):
           bar.inc(20)

When usage of a context manager is undesirable, use ``jabbar.finish()`` to clean up the output.

Further examples can be found in the `example/howto.ipynb <https://github.com/yannikschaelte/jabbar/blob/master/example/howto.ipynb>`_ notebook.


License
-------

jabbar is available under an MIT license.


.. |build| image:: https://github.com/yannikschaelte/jabbar/workflows/CI/badge.svg
   :target: https://github.com/yannikschaelte/jabbar/actions
   :alt: Build status


.. |coverage| image:: https://codecov.io/gh/yannikschaelte/jabbar/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/yannikschaelte/jabbar


.. |pypi| image:: https://img.shields.io/pypi/v/jabbar.svg
   :target: https://pypi.org/project/jabbar/
   :alt: Current version on PyPI


.. |shell| image:: https://raw.githubusercontent.com/yannikschaelte/jabbar/master/example/shell.gif
   :alt: Animation of jabbar in use
