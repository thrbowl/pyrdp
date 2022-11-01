#!/usr/bin/env python3
# coding=utf-8

#
# This file is part of the PyRDP project.
# Copyright (C) 2019-2021 GoSecure Inc.
# Licensed under the GPLv3 or later.
#

# setuptools MUST be imported first, otherwise we get an error with the ext_modules argument.
from setuptools import Extension, setup

setup(
    #packages=setuptools.find_packages(include=["pyrdp", "pyrdp.*"]),
    ext_modules=[Extension('rle', ['ext/rle.c'])],
    scripts=[
        'bin/pyrdp-clonecert.py',
        'bin/pyrdp-mitm.py',
        'bin/pyrdp-player.py',
        'bin/pyrdp-convert.py',
    ],

    install_requires=[
        'appdirs>=1,<2',
        'cryptography>=3.3.2,<37',
        'names>=0,<1',
        'progressbar2>=3.20,<5',
        'pyasn1>=0,<1',
        'pycryptodome>=3.5,<4',
        'pyopenssl>=19,<22',
        'pytz',
        'rsa>=4,<5',
        'scapy>=2.4,<3',
        'service_identity>=18',
        'twisted>=18',
    ],
    extras_require={
        "full": [
            'wheel>=0.34.2',
            'av>=8,<9',
            'PySide2>=5.12,<6',
            'qimage2ndarray>=1.6,<2',
            'py-notifier>=0.3.0',
            'win10toast>=0.9;platform_system=="Windows"',
        ]
    }
)
