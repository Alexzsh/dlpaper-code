#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
import numpy as np
def func(s):
    l = len(s)
    dp = np.zeros((l,l),dtype=np.int)

    for i in range(l):
        dp[i][i]=1
        for j in range(i-1,-1,-1):
            if s[i]==s[j]:
                dp[i][j]=dp[i-1][j+1]+2
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j+1])
    print(dp[l-1][0])
if __name__ == '__main__':
    func('abcddcgg')
    