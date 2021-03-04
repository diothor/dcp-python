from __future__ import annotations
from typing import Optional


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value: int):
        self.stack.append(value)

    def pop(self) -> Optional[int]:
        return self.stack.pop() if self.stack else None

    def peek(self) -> Optional[int]:
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return not self.stack
