#!/usr/bin/env python
try:
    from setuptools import setup
except:
    from distutils.core import setup

from mexe import __version__

setup(
    name='mexe',
    version=__version__,
    description='a script for making .py files executable',
    url='https://github.com/SanketDG/mexe',
    author='Sanket Dasgupta',
    author_email='sanketdasgupta@gmail.com',
    license='MIT',
    py_modules=['mexe'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mexe=mexe:main'
        ],
    },
)
