class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_lst = [[] for i in range(len(nums)+1)]
        count_dict = {}
        top_k = []

        for num in nums:
          count_dict[num] =  1 + count_dict.get(num,0)

        for ky,v in count_dict.items():
            count_lst[v].append(ky)
        counter = 0
        for counts in count_lst[::-1]:
            for e in counts:
                top_k.append(e)
                counter += 1
                if counter == k:
                    return top_k
            
        