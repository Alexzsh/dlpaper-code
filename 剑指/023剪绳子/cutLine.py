#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
Class Solution:
    def cut(length):
        if length<2:
            return 0
        if length==2:
            return 1
        if length==3:
            return 2
        res=[0]*length
        res[:3]=range(4)
        for i in range(4,length+1):
            maxRes=0
            for j in range(1,int(i/2)):
                maxRes=max(maxRes,res[i-j]*res[j])
                res[i]=maxRes
        return res[length]

