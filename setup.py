#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: xuyaoqiang
@contact: xuyaoqiang@gmail.com
@date: 2017-12-05 19:40
@version: 0.0.0
@license:
@copyright:

"""
import codecs
import os
import re

from setuptools import setup, find_packages

setup(
    name = "health_check",
    description = "Python Client for backend service checking",
    url = "http://github.com/xuyaoqiang/health_check",
    packages = find_packages(
        where = '.',
        exclude = ['tests', 'example.py']),
    version = '0.0.1',
    author = "xuyaoqiang",
    install_requires = [
        'requests',
        'redis',
        'pymongo',
        'kafka',
        'elasticsearch'
    ]
)

