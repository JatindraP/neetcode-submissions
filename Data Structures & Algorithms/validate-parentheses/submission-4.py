class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')':'(','}':'{',']':'['
        }
        for b in s:
            if b not in brackets.keys():
                stack.append(b)
            elif stack and b in brackets.keys() and brackets[b] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
