#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead==None:
            return None
        pNode=pHead
        while pNode:
            temp = RandomListNode(pNode.label)
            temp.next=pNode.next
            pNode.next=temp
            pNode=temp.next
        pNode=pHead
        while pNode:
            if pNode.random!=None:
                pNode.next.random=pNode.random.next
            pNode=pNode.next.next
        pNode = pHead
        pCloneHead = None
        pCloneNode = None
        if pNode:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode:
            pCloneNode.next, pCloneNode = pNode.next, pCloneNode.next
            pNode.next, pNode = pCloneNode.next, pNode.next
        return pCloneHead
