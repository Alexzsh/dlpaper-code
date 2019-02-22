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
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root==None:
            return None
        if root.left==None and root.right ==None:
            return root
        temp = root.left
        root.left = self.Mirror(root.right)
        root.right = self.Mirror(temp)
        return root
     
            
