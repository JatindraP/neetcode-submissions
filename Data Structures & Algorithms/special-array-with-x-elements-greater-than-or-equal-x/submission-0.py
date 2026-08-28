class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_value = max(nums)
        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1
        for i in range(max_value,-1,-1):
            num = 0
            for k,v in count.items():
                if k>=i:
                    num += v
            if num == i:
                return i
        return -1
        