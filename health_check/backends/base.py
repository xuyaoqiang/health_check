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
import copy
import time

class BaseBackendChecker(object):

    def __init__(self, name, *args, **kwargs):
        self._name = name
        self._time_cost = 0 
        self._errors = []
        self._status = {}
        self._config = copy.deepcopy(kwargs)
    
    @property
    def name(self):
        return self._name

    @property
    def status(self):
        data = dict(name = self._name, 
                    healthy = self.healthy 
                    )

        if not self.healthy:
            data.update(dict(errors=[str(e) for e in self._errors]))

        if self._status:
            data.update(self._status)

        data.update(dict(time_cost=self._time_cost))

        return data
 
    @property
    def healthy(self):
        return not self._errors

    @property
    def config(self):
        return self._config

    def run(self):
        start = time.time()
        try:
            self._status = dict(status=self.check_status())
        except Exception as e:
            self._errors.append(e)
        finally:
            self._time_cost = time.time() - start 

    def check_status(self):
        raise NotImplementedError

