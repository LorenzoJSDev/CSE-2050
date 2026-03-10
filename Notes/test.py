class Stack():
    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)

    def pop(self):
        try:
            return self._list.pop()
        except:
            raise ValueError("Can not pop from an empty stack")

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return len(self._list) == 0

s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.pop(),s.pop(),s.pop())

print(s.is_empty())