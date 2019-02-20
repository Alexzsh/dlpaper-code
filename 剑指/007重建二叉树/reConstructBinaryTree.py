# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        
        if len(pre)==0 or len(tin)==0:
            return None
        root = TreeNode(pre[0])
        index = [indexx for indexx,i in enumerate(tin) if i == root.val][0]
        root.left = self.reConstructBinaryTree(pre[1:index+1],tin[:index])
        root.right = self.reConstructBinaryTree(pre[index+1:],tin[index+1:])
        return root
