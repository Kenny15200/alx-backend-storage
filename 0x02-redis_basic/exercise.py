#!/usr/bin/env python3
"""
Cache module for storing and retrieving data from Redis.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of calls to a method.
    
    Args:
        method: The method to be decorated.
    
    Returns:
        Callable: The wrapped method with call count functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment the call count."""
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs of a method.
    
    Args:
        method: The method to be decorated.
    
    Returns:
        Callable: The wrapped method with call history functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store call history."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper

class Cache:
    """Cache class to interact with Redis."""
    def __init__(self):
        """Initialize the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the key.
        
        Args:
            data: Data to be stored, can be str, bytes, int, or float.
        
        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally convert it to the desired format.
        
        Args:
            key: The key to retrieve.
            fn: Optional callable to convert the data.
        
        Returns:
            The retrieved data in the desired format or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.
        
        Args:
            key: The key to retrieve.
        
        Returns:
            str: The retrieved string or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.
        
        Args:
            key: The key to retrieve.
        
        Returns:
            int: The retrieved integer or None if the key does not exist.
        """
        return self.get(key, lambda d: int(d))

