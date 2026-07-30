class Solution:
    def isValid(self, s: str) -> bool:
        opening = set(['(','{','['])
        closing = set([')','}',']'])
        stack = []
        for p in s:
            if p in opening:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                le = stack.pop()
                if (p==')' and le != '(') or (p=='}' and le != '{') or (p==']' and le != '['):
                    return False
        if len(stack) != 0:
            return False
        
        return True
        