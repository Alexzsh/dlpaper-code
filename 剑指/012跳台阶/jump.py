#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        dp=[0]*1000
        dp[1]=1
        dp[2]=2
        for i in range(3,1000):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[number]
