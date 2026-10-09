class MinStack:
    def __init__(self):
        self.s = []

    def push(self, value: int) -> None:
        if not self.s:
            self.s.append((value, value))
        else:
            minval = min(value, self.s[-1][1])
            self.s.append((value, minval))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]