# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        left = 0
        right = len(array)-1
        rightLen = right
        while left < right:
            while array[right] % 2 != 0 and left < right:
                right -= 1
            if left <= right and array[right] % 2 == 0:
                for i in range(right+1, rightLen+1):
                    if array[i] % 2 != 0:
                        temp = array[right]
                        array[right] = array[i]
                        array[i] = temp
                        right = i
                rightLen -= 1
                right = rightLen
        return array
