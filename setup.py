"""Setup jabbar module."""

import os
import setuptools

# extract version
with open(os.path.join(os.path.dirname(__file__), "jabbar", "version.py")) as f:
    version = f.read().split("\n")[0].split("=")[-1].strip(' ').strip("'")

# all other information comes from setup.cfg

if __name__ == '__main__':
    setuptools.setup(version=version)
