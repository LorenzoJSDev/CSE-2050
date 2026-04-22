"""
Author: Lorenzo .S
Date: 4/14/2026

Notes:
    None
"""
"""
Implement the rehash(self) method.

Your method should:

Double the size of the hash table,
Create a new list of empty buckets,
Reinsert all existing key-value pairs into the new buckets using hashing.
"""


class HashMapping:
    def __init__(self, size=2):
        self._size = size
        self._buckets = [ListMapping()] * self._size
        self._length = 0

    def _bucket(self, key):
        return self._buckets[hash(key) % self._size]

    def rehash(self):
        #Save old buckets
        old_buckets = self._buckets

        #Double the size of the hash table
        self._size = self._size * 2

        #Create a new list of empty buckets
        self._buckets = [ListMapping()] * self._size

        #Reinsert all existing key-value pairs into the new buckets using hashing
        for bucket in old_buckets:
            for item in bucket
                self._bucket(item.key).put(item.key,item.value)