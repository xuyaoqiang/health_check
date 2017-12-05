#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: xuyaoqiang
@contact: xuyaoqiang@gmail.com
@date: 2017-12-05 14:06
@version: 0.0.0
@license:
@copyright:

"""
import redis
from health_check.backends.base import BaseBackendChecker


class RedisChecker(BaseBackendChecker):

    def check_status(self):
        uri = self.config.get('uri', '') 
        try:
            client = redis.Redis(uri)
            return client.info()
        except Exception as e:
            self._errors.append(e)
            
