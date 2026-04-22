"""
Author: Lorenzo .S
Date: 4/14/2026


Notes:
    None
"""

"""
Implement the get(self, key) method such that:

If the key exists, return its value.
If the key does not exist, raise a KeyError.
"""

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class ListMapping:
    def __init__(self):
        self._entries = []

    def put(self, key, value):
        for e in self._entries:
            if e.key == key:
                e.value = value
                return
        self._entries.append(Entry(key, value))

    def get(self, key):
        for e in self._entries:
            if e.key == key:
                return e.value
        raise KeyError("This key does not exist in the list")


m = ListMapping()
m.put("x", 10)
m.put("y", 20)

print(m.get("x"))  # returns 10
m.get("z")  # raises KeyError



