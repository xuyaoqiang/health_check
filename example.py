#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: xuyaoqiang
@contact: xuyaoqiang@gmail.com
@date: 2017-12-05 19:55
@version: 0.0.0
@license:
@copyright:

"""


from health_check import HealthChecker, RedisChecker, MongodbChecker


if __name__ == "__main__":
    health = HealthChecker()

    health.add_checker(RedisChecker('redis', uri='localhost'))
    health.add_checker(MongodbChecker('mongodb', uri='mongodb://localhost:27017/unittest'))
    health.run()
    print(health.status)
