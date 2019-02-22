#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res=False
        if pRoot1==None or pRoot2==None:
            return res
        if pRoot1.val==pRoot2.val:
            res=self.func(pRoot1,pRoot2)
        if not res:
            res=self.HasSubtree(pRoot1.left,pRoot2)
        if not res:
            res=self.HasSubtree(pRoot1.right,pRoot2)
        return res
    def func(self,p1,p2):
        if p2==None:
            return True
        if p1==None:
            return False
        if p1.val!=p2.val:
            return False
        return self.func(p1.left,p2.left) and self.func(p1.right,p2.right)

