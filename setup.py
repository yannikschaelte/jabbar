"""Setup jabbar module."""

import os

import setuptools

# extract version
base = os.path.dirname(__file__)
with open(os.path.join(base, 'jabbar', 'version.py')) as f:
    version = f.read().split('\n')[-2].split('=')[-1].strip(' ').strip("'")

# all other information comes from setup.cfg

if __name__ == '__main__':
    setuptools.setup(version=version)
