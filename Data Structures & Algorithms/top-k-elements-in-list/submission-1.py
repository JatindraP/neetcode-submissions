class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in  range(0,len(nums) + 1)]
        top_k = []
        for n in nums:
            count[n] = 1 + count.get(n,0)

        for key,val in count.items():
            frequency[val].append(key)

        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k
            
        