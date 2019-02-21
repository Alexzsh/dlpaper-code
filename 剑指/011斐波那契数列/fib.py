#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=1:
            return n
        dp = [0]*40
        dp[1]=1
        dp[2]=1
        for i in range(3,40):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
            
