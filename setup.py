#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "Mini-NDN",
    version = '0.4.0',
    packages = find_packages(),
    scripts = ['bin/minindn', 'bin/minindnedit'],
)
