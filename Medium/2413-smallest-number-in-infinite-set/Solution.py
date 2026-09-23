class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.added = []
        self.inHeap = set()

    def popSmallest(self) -> int:
        if self.added:
            val = heapq.heappop(self.added)
            self.inHeap.remove(val)
            return val
        val = self.curr
        self.curr += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.inHeap:
            heapq.heappush(self.added,num)
            self.inHeap.add(num)
