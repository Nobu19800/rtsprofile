#!/usr/bin/env python3
# -*- Python -*-
# -*- coding: utf-8 -*-

'''rtsprofile

Copyright (C) 2009-2015
    Geoffrey Biggs
    RT-Synthesis Research Group
    Intelligent Systems Research Institute,
    National Institute of Advanced Industrial Science and Technology (AIST),
    Japan
    All rights reserved.
Licensed under the GNU Lesser General Public License version 3.
http://www.gnu.org/licenses/lgpl-3.0.en.html

File: setup.py

Install script.

'''

__version__ = '$Revision: $'
# $Source$


import setuptools
import sys


setuptools.setup(name='rtsprofile-aist',
      version='4.1.5',
      description='Library to read, manipulate and write RT system profiles \
using the RTSProfile XML schema.',
      long_description='Library to read, manipulate and write RT system \
profiles using the RTSProfile XML schema.',
      author='Geoffrey Biggs, Noriaki Ando',
      author_email='n-ando@aist.go.jp',
      url='https://github.com/OpenRTM/rtsprofile',
      license='LGPL3',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development',
          ],
      packages=['rtsprofile'],
      include_package_data = True,
      zip_safe = True
      )

#  vim: set ts=2 sw=2 tw=79 :

