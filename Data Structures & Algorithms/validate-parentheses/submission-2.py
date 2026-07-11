from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                if i != pairs[stack.pop()]:
                    return False

        return not stack