class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #create minheap using nums
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while(len(self.minheap) > self.k):
            heapq.heappop(self.minheap)  

    def add(self, val: int) -> int:
        if len(self.minheap) >= self.k and val < self.minheap[0]:
            return self.minheap[0]
        else:
            heapq.heappush(self.minheap, val)
            while(len(self.minheap) > self.k):
                heapq.heappop(self.minheap)
            return self.minheap[0]
        
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)