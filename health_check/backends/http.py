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
import requests
from health_check.backends.base import BaseBackendChecker


class HTTPChecker(BaseBackendChecker):

    def check_status(self):
        url = self.config.get('url', '') 
        try:
            resp = requests.get(url)
            if resp.status_code < 400:
                return dict(status=resp.status_code)
            else:
                raise Exception()
        except Exception as e:
            self._errors.append(e)
        
