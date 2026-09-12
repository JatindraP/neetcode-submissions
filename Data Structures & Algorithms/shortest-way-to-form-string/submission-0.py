class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        idx=res = 0
        while idx < len(target):
            prev_idx = idx
            for c in source:
                if idx < len(target) and c == target[idx]:
                    idx += 1
            if prev_idx == idx:
                return -1
            res += 1
        return res
        