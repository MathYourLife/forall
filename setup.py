#!/usr/bin/env python

import os
from setuptools import setup

REQ_FILE = os.path.join(os.path.dirname(__file__), 'requirements.txt')

# Pull required packages from the requirements.txt file
with open(REQ_FILE) as rfile:
    required = rfile.read().strip().split('\n')

setup(
    name='forall',
    packages=['forall'],
    package_dir={'':'src'},
    license='MIT license',
    install_requires=required,
)
