"""
Author: Lorenzo .S
Date: 4/13/2026


Notes:
    None
"""
from list_mapping import ListMapping


"""
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
        self._size = self._size * 2
        old_buckets = self._buckets
        self._buckets = [ListMapping()] * self._size
        for bucket in old_buckets:
            for key in bucket:
                self._bucket(key)

