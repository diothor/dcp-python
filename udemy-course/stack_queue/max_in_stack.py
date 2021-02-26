from __future__ import annotations
from typing import Optional
from stack_queue.stack import Stack


class StackWithMax(Stack):

    def __init__(self):
        super().__init__()
        self.max_value = []

    def push(self, new_element):
        if not self.max_value or self.max_value[-1] <= new_element:
            self.max_value.append(new_element)
        elif self.max_value[-1] > new_element:
            self.max_value.append(self.max_value[-1])
        super().push(new_element)

    def pop(self) -> Optional[int]:
        if self.max_value:
            del self.max_value[-1]
        return super().pop()

    def max(self) -> Optional[int]:
        return self.max_value[-1] if self.max_value else None
