"""
lab10.py

Priority Queue ADT implemented with:
- PQ_UL: unordered list
- PQ_OL: ordered list
"""

class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return (
            isinstance(other, Entry)
            and self.item == other.item
            and self.priority == other.priority
        )

    def __repr__(self):
        return f"Entry({self.item!r}, {self.priority!r})"


class PQ_UL:
    def __init__(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))

    def find_min(self):
        if len(self._entries) == 0:
            raise IndexError("find_min from empty priority queue")
        return min(self._entries)

    def remove_min(self):
        if len(self._entries) == 0:
            raise IndexError("remove_min from empty priority queue")

        min_index = 0
        for i in range(1, len(self._entries)):
            if self._entries[i] < self._entries[min_index]:
                min_index = i

        return self._entries.pop(min_index)


class PQ_OL:
    def __init__(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)

    def insert(self, item, priority):
        new_entry = Entry(item, priority)

        index = 0
        while index < len(self._entries) and self._entries[index].priority <= priority:
            index += 1

        self._entries.insert(index, new_entry)

    def find_min(self):
        if len(self._entries) == 0:
            raise IndexError("find_min from empty priority queue")
        return self._entries[0]

    def remove_min(self):
        if len(self._entries) == 0:
            raise IndexError("remove_min from empty priority queue")
        return self._entries.pop(0)