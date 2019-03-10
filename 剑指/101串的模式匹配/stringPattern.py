#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-

class StringPattern:
    def getNext(self,s):
        length = len(s)
        nextArray=[-1]*length
        i=0
        j=-1
        while i<length-1:
            if j==-1 or s[i]==s[j]:
                i+=1
                j+=1
                nextArray[i]=j
            else:
                j = nextArray[j]
        return nextArray

    def findAppearance(self, A, lena, B, lenb):
        # write code here
        nextArray = self.getNext(A)
        i=0
        j=0
        while i<lena and j<lenb:
            if j==-1 or A[i]==B[j]:
                i+=1
                j+=1
            else:
                j=nextArray[j]
        if j==lenb:
            return i-j
        else:
            return -1
if __name__ == '__main__':
    StringPattern().findAppearance('abababcd',8,'abcd',4)
    