jabbar
======

|build| |pypi|

Just Another Beautiful progress BAR (some might replace Beautiful by Boring).

jabbar is a python package implementing a simple progress bar. The output
looks like:

.. code-block:: sh

   75% |█████████████████      | 750/1000

It is lightweight, and easy to use and modify.
As a special feature, it can deal with more items than expected, e.g.
1100/1000.

Install
-------

jabbar can be installed from `PyPI <https://pypi.org/project/jabbar>`_ via

.. code-block:: sh

   $ pip install jabbar

or from the latest code on `GitHub <https://github.com/yannikschaelte/jabbar>`_ with

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
   with jabbar(total=1000) as bar:
       for _ in range(50):
           bar.inc(20)

When usage of a context manager is undesirable, use ``jabbar.finish()`` to
finish the output line.


License
-------

jabbar is available under a MIT license.

.. |build| image:: https://github.com/yannikschaelte/jabbar/workflows/CI/badge.svg
   :target: https://github.com/yannikschaelte/jabbar/actions
   :alt: Build status


.. |pypi| image:: https://img.shields.io/pypi/v/jabbar.svg
   :target: https://pypi.org/project/jabbar/
   :alt: Current version on PyPI
