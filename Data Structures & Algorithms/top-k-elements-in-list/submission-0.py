class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = {}
        for num in nums:
            number_count[num] = 1+number_count.get(num,0)
        number_count_order = dict(sorted(
            number_count.items(),key=lambda item : item[1],
            reverse = True
        ))
        keys = list(number_count_order.keys())
        return keys[:k]