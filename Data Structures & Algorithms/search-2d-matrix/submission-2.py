class Solution:
    def binarySearch(self,nums: List[int],target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m+1
            else:
                r = m -1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_l, m_r = 0, len(matrix) - 1
        while m_l <= m_r:
            m_m = (m_l+m_r) // 2
            if matrix[m_m][0] <= target <= matrix[m_m][len(matrix[m_m])-1]:
                return self.binarySearch(matrix[m_m],target)
            elif target < matrix[m_m][0]:
                m_r = m_m - 1
            else:
                m_l = m_m + 1
        return False
        