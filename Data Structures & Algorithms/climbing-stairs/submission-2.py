class Solution:
    def __init__(self):
        self.seen = [-1]*(45+1)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if self.seen[n-1] == -1:
            self.seen[n-1] = self.climbStairs(n-1)
        if self.seen[n-2] == -1:
            self.seen[n-2] = self.climbStairs(n-2)
        return self.seen[n-1] + self.seen[n-2]