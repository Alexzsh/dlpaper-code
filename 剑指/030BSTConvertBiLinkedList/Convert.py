# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def Fun(self, pRoot):
        global pLastNode
        if pRoot == None:
            return
        pCur = pRoot
        if pCur.left != None:
            self.Fun(pCur.left)
        pCur.left = pLastNode
        if pLastNode != None:
            pLastNode.right = pCur
        pLastNode = pCur
        if pCur.right != None:
            self.Fun(pCur.right)

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        res = pRootOfTree
        while res.left:
            res = res.left
        global pLastNode
        pLastNode = None
        self.Fun(pRootOfTree)
        return res
