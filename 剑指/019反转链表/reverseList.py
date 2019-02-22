#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here

        pCur = pHead
        pPre = None
        pRes = None
        if pHead==None or pHead.next==None :
            return pHead
        while pCur!=None:
            pNext = pCur.next
            if pNext!=None:
                pRes=pNext
            pCur.next=pPre
            pPre = pCur
            pCur = pNext
        return pRes
