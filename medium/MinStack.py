# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        self.data = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minimums or val < self.minimums[-1]:
            self.minimums.append(val)
        else:
            self.minimums.append(self.minimums[-1])

    def pop(self) -> None:
        self.data.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
