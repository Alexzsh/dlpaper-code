#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        res=0
        while n&0xffffffff !=0:
            n&=n-1
            res+=1
        return res#relate on:

