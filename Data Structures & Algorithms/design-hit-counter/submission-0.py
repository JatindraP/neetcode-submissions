class HitCounter:

    def __init__(self):
        self.hits=[]
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        start_hit = timestamp - 300
        count=i=0
        while i<len(self.hits) and self.hits[i]<=timestamp:
            if self.hits[i]>start_hit:
                count+=1
            i+=1
        return count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)