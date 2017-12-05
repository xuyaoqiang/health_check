#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: xuyaoqiang
@contact: xuyaoqiang@gmail.com
@date: 2017-12-05 19:35
@version: 0.0.0
@license:
@copyright:

"""


class HealthCheckException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
