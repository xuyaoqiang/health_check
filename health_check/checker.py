#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: xuyaoqiang
@contact: xuyaoqiang@gmail.com
@date: 2017-12-05 13:31
@version: 0.0.0
@license:
@copyright:

"""
from health_check.exceptions import HealthCheckException
from health_check.backends.base import BaseBackendChecker


class HealthChecker(object):

    def __init__(self):
        self._checkers = {} 
        self._status = {}

    def add_checker(self, checker):
        if not isinstance(checker, BaseBackendChecker):
            raise HealthCheckException("checker should be instance of BaseBackendChecker") 
        if checker.name in self._checkers:
            raise HealthCheckException("duplicate checker!")
        self._checkers[checker.name] = checker

    def run(self):
        """
        Run all checkers and return a dict containing backends status and 
        boolean to indicate to if all backends are healthy
        """
        healthy = True
        for name in self._checkers:
            checker = self._checkers[name]
            checker.run()
            if not checker.healthy:
                healthy = False
            self._status[checker.name] = checker.status
        self._status['healthy'] = healthy
        return self.status
   
    @property
    def status(self):
        return self._status

