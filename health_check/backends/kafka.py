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
from kafka import SimpleClient 
from health_check.backends.base import BaseBackendChecker


class KafkaChecker(BaseBackendChecker):

    def check_status(self):
        host = self.config.get('host', '') 
        try:
            client = SimpleClient(hosts=host)
            return dict(topics=client.topics)
        except Exception as e:
            self._errors.append(e)
        
