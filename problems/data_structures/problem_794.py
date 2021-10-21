from typing import Any


class StackWithMax:

    def __init__(self):
        self.values = []
        self.maxes = []

    # O(1)
    def push(self, val) -> None:
        new_max = max(val, self.maxes[-1] if self.maxes else float('-inf'))
        self.values.append(val)
        self.maxes.append(new_max)

    # O(1)
    def peek(self) -> Any:
        return self.values[-1] if self.values else None

    # O(1)
    def pop(self) -> Any:
        if not self.values:
            return None
        self.maxes.pop()
        return self.values.pop()

    # O(1)
    def max_val(self) -> Any:
        if not self.maxes:
            return None
        return self.maxes[-1]


stack = StackWithMax()
assert stack.pop() is None
assert stack.max_val() is None

stack.push(2)
assert stack.peek() == 2
assert stack.max_val() == 2

stack.push(1)
assert stack.peek() == 1
assert stack.max_val() == 2

stack.push(3)
assert stack.peek() == 3
assert stack.max_val() == 3

assert stack.pop() == 3
assert stack.pop() == 1
assert stack.pop() == 2
assert stack.pop() is None
