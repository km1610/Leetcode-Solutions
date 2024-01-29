class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while self.q1:
            self.q2.append(self.q1.pop())
        popped = self.q2.pop()
        while self.q2:
            self.q1.append(self.q2.pop())
        return popped        

    def peek(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        if self.q1:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
