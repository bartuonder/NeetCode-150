class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if len(self.my_stack) == 0:
            return None
        self.min_stack.pop()
        return self.my_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]