# -*- coding: utf-8 -*-
from __future__ import absolute_import

from health_check.checker import HealthChecker
from health_check.backends.redis import RedisChecker
from health_check.backends.mongodb import MongodbChecker
from health_check.backends.elasticsearch import ESChecker
from health_check.backends.kafka import KafkaChecker
from health_check.backends.http import HTTPChecker

version = (0, 0, 1)

__version__ = '.'.join([str(i) for i in version])


__all__ = [
    __version__,
    'HealthChecker',
    'RedisChecker',
    'MongodbChecker',
    'ESChecker',
    'KafkaChecker',
    'HTTPChecker',
]
