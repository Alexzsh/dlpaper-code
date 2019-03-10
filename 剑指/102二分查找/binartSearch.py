#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
class BinarySearch:
    def getPos(self, A, n, val):
        # write code here
        if n==0:
            return -1
        start = 0
        end = n
        res=-1
        while start<=end:
            mid = (start+end) >> 1
            if A[mid]==val:
                res = mid
                break
            elif A[mid]>val:
                end = mid-1
            else:
                start = mid+1
        if res!=-1:
            while A[res-1]==val:
                res-=1
        return res
if __name__ == '__main__':
    BinarySearch().getPos([1,3,3,3,3,3,5,7,9],5,3)    
    
