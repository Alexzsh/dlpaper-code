import random


class Solution:
    def partrition(self, num, start, end):
        mid = start+(end-start) >> 1
        index = random.randint(start, end)
        change = start-1
        num[index], num[end] = num[end], num[index]
        for i in range(start, end):
            if num[i] < num[end]:
                change += 1
                num[i], num[change] = num[change], num[i]
        change += 1
        num[change], num[end] = num[end], num[change]
        return change

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == None or k > len(tinput) or k == 0:
            return []
        start = 0
        end = len(tinput)-1
        index = self.partrition(tinput, start, end)
        while index != k-1:
            if index > k-1:
                end = index-1
            else:
                start = index+1
            index = self.partrition(tinput, start, end)
        return sorted(tinput[:k])
