#!/usr/bin/env python

import codecs
import os
import re
import sys

from setuptools import setup, find_packages


setup_requires = []

tests_require = [
    'pytest>=3.0.0',
]

install_requires = [
    'pyex',
    'quandl',
    'pandas',
    'numpy',
    'matplotlib',
    'scipy',
    'scikit-learn',
    'h5py',
    'tensorflow',
    'keras',
    'fbprophet'
]

setup(
    name='models',
    description='Malgo ML models',
    python_requires='>=3.0.0',
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: Unstable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
    ]
)
