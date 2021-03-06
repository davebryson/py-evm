#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


DIR = os.path.dirname(os.path.abspath(__file__))


readme = open(os.path.join(DIR, 'README.md')).read()


setup(
    name='py-evm',
    version="0.1.0",
    description="""Python implementation of the Ethereum Virtual Machine""",
    long_description=readme,
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/pipermerriam/py-evm',
    include_package_data=True,
    py_modules=['evm'],
    install_requires=[
        "ethereum-utils>=0.2.0",
        "rlp==0.4.7",
        "trie>=0.2.4",
        "ethereum-bloom>=0.3.0",
    ],
    license="MIT",
    zip_safe=False,
    keywords='ethereum blockchain evm',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
