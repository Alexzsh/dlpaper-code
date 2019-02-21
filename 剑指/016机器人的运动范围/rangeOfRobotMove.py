#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
class Solution(object):
    directs = [(1,0), (-1,0), (0,1), (0,-1) ]
    @staticmethod
    def sumNum(m):
        res=0
        while m:
            res+=m%10
            m=int(m/10)
        return res
    @classmethod 
    def func(cls,m, n,k):
        if m<=0 or n<=0 or k<=0:
            return 0
        visited=[False]*m*n
        res = cls.rangeOfRobotMove(m, n, 0, 0, k, visited)
        return res

    @classmethod
    def rangeOfRobotMove(cls,m, n, i, j, k, visited):

        sumRes=0
        if i >= 0 and i < m and j >= 0 and j < n and cls.sumNum(i)+cls.sumNum(j) <= k and not visited[i*n+j]:
            visited[i*n+j]=True
            sumRes=1
            for direct in cls.directs:
                sumRes+=cls.rangeOfRobotMove(m,n,i+direct[0],j+direct[1],k,visited)
        return sumRes
        
       
print(Solution.func(4,4,4))
