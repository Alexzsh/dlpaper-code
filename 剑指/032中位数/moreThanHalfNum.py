#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-
import random


class Solution:

    def partrition(self, numList, start, end):

        mid = start+(end-start) >> 1
        index = random.randint(start, end)
        numList[end], numList[index] = numList[index], numList[end]
        change = start-1
        for i in range(start, end):
            if numList[i] < numList[end]:
                change += 1
                if change != i:
                    numList[change], numList[i] = numList[i], numList[change]

        change += 1
        numList[end], numList[change] = numList[change], numList[end]
        return change

    def check(self, numbers, number):
        res = 0
        for i in numbers:
            if i == number:
                res += 1
        if res*2 <= len(numbers):
            return False
        return True

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == None or len(numbers) == 0:
            return None
        res = numbers
        start = 0
        mid = len(numbers) >> 1
        end = len(numbers)-1
        index = self.partrition(numbers, start, end)
        while index != mid:
            if index > mid:
                end = index-1
            elif index < mid:
                start = index+1
            index = self.partrition(numbers, start, end)
        return numbers[mid] if self.check(numbers, numbers[mid]) else 0

if __name__ == '__main__':
    Solution().MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2])
    
