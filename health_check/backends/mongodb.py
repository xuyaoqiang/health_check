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
import pymongo
from health_check.backends.base import BaseBackendChecker


class MongodbChecker(BaseBackendChecker):

    def check_status(self):
        uri = self.config.get('uri', '') 
        try:
            conn = pymongo.MongoClient(uri)
            return conn.get_default_database().command('dbstats')
        except Exception as e:
            self._errors.append(e)
        
