from __future__ import annotations
from typing import Optional, Any
from stack_queue.stack import Stack


class QueueOnStack:

    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    # O(1)
    def enqueue(self, elem: Any) -> QueueOnStack:
        self.front.push(elem)
        return self

    # O(1)+ (amortized constant time)
    def dequeue(self) -> Optional[Any]:
        if self.rear.is_empty():
            while not self.front.is_empty():
                self.rear.push(self.front.pop())
        return self.rear.pop()
