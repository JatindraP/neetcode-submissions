class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = {'+','C','D'}
        for o in operations:
            if o not in ops:
                stack.append(int(o))
            elif o == '+':
                priv1 = stack[-1]
                priv2 = stack[-2]
                stack.append(priv1+priv2)
            elif o == 'C':
                stack.pop()
            else:
                prev = stack[-1]
                stack.append(prev*2)
        return sum(stack)


        