#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
import heapq
class Solution:
    class topKSmall(object):
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

        def getSmall(self):
            return self.data[0]

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
            return [x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]

        def getLarge(self):
            return -self.data[0]

    def check(self, numbers, number):
        res = 0
        for i in numbers:
            if i == number:
                res += 1
        if res*2 <= len(numbers):
            return False
        return True
    def MoreThanHalfNum_Solution(self, listNum):
        if len(listNum)%2:
            small = (len(listNum) >> 1)+1
        else:
            small = len(listNum)>>1
        large = len(listNum)-small
        thSmall = self.topKSmall(small)
        thLarge = self.topKLarge(large)
        for i in listNum:
            res = thSmall.push(i)
            if res == None:
                continue
            else:
                thLarge.push(-res)
        res = thSmall.getSmall() 
        return res if self.check(listNum, res) else 0


if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution([1]))
