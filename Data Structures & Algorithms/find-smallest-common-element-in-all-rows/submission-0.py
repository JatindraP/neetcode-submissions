class Solution:
    def binary(self,arr: List[int],n: int) -> bool:
        l,r = 0,len(arr)-1
        while l<=r:
            m = (l+r)//2
            if arr[m]<n:
                l = m+1
            elif arr[m]>n:
                r = m-1
            else:
                return True
        return False
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        l,r=0,float('inf')
        for m in mat:
            l = max(l,m[0])
            r = min(r,m[-1])

        is_present = True
        for i in range(l,r+1):
            for arr in mat:
                is_present = is_present and self.binary(arr,i)
            if is_present:
                return i
            else:
                is_present = True
        return -1
        