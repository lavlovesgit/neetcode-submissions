from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        

        self.stack1.append(x)

    def pop(self) -> int:
        if(not self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if(not self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        else:
            return True