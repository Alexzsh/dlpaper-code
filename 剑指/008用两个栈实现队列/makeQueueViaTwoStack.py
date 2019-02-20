#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-

class Solution:
    def __init__(self):
        self.first = []
        self.second = []
    def push(self, node):
        # write code here
        self.first.append(node)
    def pop(self):
        # return xx
        if len(self.first)==0 and len(self.second)==0:
            return
        elif len(self.second)==0:
            while len(self.first)>0:
                self.second.append(self.first.pop())
        return self.second.pop() 
