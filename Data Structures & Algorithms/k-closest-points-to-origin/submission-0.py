class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        meanHeap = []
        for x,y in points:
            dis = (x**2)+(y**2)
            meanHeap.append([dis,x,y])
        heapq.heapify(meanHeap)
        res = []
        while k>0 :
            dis,x,y = heapq.heappop(meanHeap)
            res.append([x,y])
            k-=1
        return res
        