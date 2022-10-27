class MyQueue:

    def __init__(self):
        ## keeping the variable private so that it can&t be accessed from outside the class
        ## solely dependent on the function calls
        self._queue = list()

    def push(self, x: int) -> None:
        ## just saving the element in the list
        self._queue.append(x)

    def pop(self) -> int:
        ## stack is a FIFO
        return self._queue.pop(0)

    def peek(self) -> int:
        ## peek only returns the first element
        ## pop returns and deletes
        return self._queue[0]

    def empty(self) -> bool:
        if self._queue:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()