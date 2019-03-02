#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)<=0 or sequence==None:
            return False
        root = sequence[-1]
        if max(sequence)<root and min(sequence)>root:
            return True
        i=0
        for k in range(len(sequence)-1):
            i=k
            if sequence[k]>root:
                break

        for k in range(i+1,len(sequence)-1):
            if sequence[k]<root:
                return False
        left = True
        if i>0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i<len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

if __name__ == '__main__':
    print(Solution().VerifySquenceOfBST([5,4,3,2,1]))
    
