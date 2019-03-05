import heapq


class Solution:
    class topKLarge(object):
        def __init__(self, k):
            self.k = k
            self.data = []

        def push(self, data):
            if len(self.data) < self.k:
                heapq.heappush(self.data, data)
                return None
            else:
                topK = self.data[0]
                if data >= topK:
                    return heapq.heapreplace(self.data, data)

        def topK(self):
            return [-x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]

        def getLarge(self):
            return -self.data[0]

    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) == 0 or k > len(tinput) or k == 0:
            return []
        heap = self.topKLarge(k)
        for i in tinput:
            heap.push(-i)
        return heap.topK()
