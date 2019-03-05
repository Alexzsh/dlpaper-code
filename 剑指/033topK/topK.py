#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
import heapq
class topKSmall(object):
    def __init__(self, k):
        self.k = k
        self.data = []
    def push(self,data):
        if len(self.data)<self.k:
            heapq.heappush(self.data,data)
            return None
        else:
            topK = self.data[0]
            if data>topK:
                return heapq.heapreplace(self.data,data)
    def getSmall(self):
        return self.data[0]
class topKLarge(object):
    def __init__(self, k):
        self.k = k
        self.data = []
    
    def push(self,data):
        if len(self.data)<self.k:
            heapq.heappush(self.data,data)
        else:
            topK = self.data[0]
            if data>topK:
                heapq.heapreplace(self.data,data)
    def topK(self):
        return [x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]
    def getLarge(self):
        return -self.data[0] 
if __name__ == '__main__':
    listNum=[1,1,1,1,2,3,4,5,6,7,8,9]
    small = len(listNum)>>1
    large = len(listNum)-small
    thSmall = topKSmall(small)
    thLarge = topKLarge(large)
    for i in listNum:
        res = thSmall.push(i)
        if res==None:
            continue
        else:
            thLarge.push(-res)
    res = thLarge.getLarge() if len(listNum)%2!=0 else (thLarge.getLarge()+thSmall.getSmall())/2
    print(res)

    
