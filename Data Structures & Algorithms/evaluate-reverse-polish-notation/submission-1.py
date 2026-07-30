class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        ops = set(['+','*','-','/'])
        for t in tokens:
            if t in ops:
                r = 0
                p2 = int(result.pop())
                p1 = int(result.pop())
                if t == '+':
                    r = p1 + p2
                elif t == '*':
                    r = p1 * p2
                elif t == '-':
                    r = p1 - p2
                elif t == '/':
                    r = p1 / p2
                result.append(r)
            else:
                result.append(t)
        return int(result[0])
        