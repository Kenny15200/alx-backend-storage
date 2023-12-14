#!/usr/bin/env python3
""" Define a class 'cache' """
import redis
from typing import Union, Callable
import uuid


class Cache:
    """ create a class cache """
    def __init__(self):
        """ initialize the cache instace """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ A menthod that generate a random key using uuid
            stores the input data in redis
            using a random key and returns the key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, 
            fn: callable = None
            ):
        """ retrives values from redis """
        data = self._redis.get(key)
        if data is not None:
            return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """ get data and converts to string """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ get data and converts to integer """
        return self.get(key, fn = lambda x: int(x))
