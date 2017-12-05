# -*- coding: utf-8 -*-

from .checker import HealthChecker
from .backends.redis import RedisChecker
from .backends.mongodb import MongodbChecker
from .backends.elasticsearch import ESChecker
from .backends.kafka import KafkaChecker
from .backends.http import HTTPChecker

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
