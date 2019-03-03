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
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.res=[[]]
    def FindPath(self, root, expectNumber):
        # write code here
        if root==None:
            return []

        self.res[-1].append(root.val)
        expectNumber-=root.val
        
        if root.left==None and root.right==None and expectNumber==0:
            self.res.append(self.res[-1][:-1])
            
            if len(self.res)==0:
                return []
            else:
                return self.res[:-1]
        if root.left!=None:
            self.FindPath(root.left,expectNumber)
        if root.right!=None:
            self.FindPath(root.right,expectNumber)
        self.res[-1].pop(-1)
        
        
        if len(self.res)==0:
            return []
        else:
            return self.res[:-1]
            
