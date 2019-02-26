# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here

        if root==None:
            return []
        a=[]
        a.append(root)
        res=[]
        while len(a)!=0 :
            b=a.pop(0)
            res.append(b.val)
            if b.left!=None:
                a.append(b.left)
            if b.right!=None:
                a.append(b.right)
        return res