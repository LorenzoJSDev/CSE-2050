"""
Author: Lorenzo .S
Date: 4/14/2026


Notes:
    Perfect execution! YES!!!
"""

"""
Implement the put(self, key, value) method such that:

If the key already exists, update its value.
Otherwise, insert a new Entry(key, value) into _entries.
"""


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class ListMapping:
    def __init__(self):
        self._entries = []

    def __iter__(self):
        return iter(self._entries)

    def put(self, key, value):
        for e in self._entries:
            if e.key == key:
                e.value = value
                return
        new_entry = Entry(key,value)
        self._entries.append(new_entry)
        return

m = ListMapping()
m.put("a", 1)
m.put("b", 2)
m.put("a", 3)

for i in m:
    print(i.value)