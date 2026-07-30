class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        right_max = -1
        result = [0]*length
        for i in range(length-1,-1,-1):
            result[i] = right_max
            right_max = max(right_max,arr[i])
        return result
        