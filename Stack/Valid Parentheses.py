class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "]": "[", "}": "{"}
        my_stack = []
        for p in s:
            if p in close_to_open:
                if not my_stack or my_stack[-1] != close_to_open[p]:
                    return False
                my_stack.pop()
            else:
                my_stack.append(p)
        return len(my_stack) == 0