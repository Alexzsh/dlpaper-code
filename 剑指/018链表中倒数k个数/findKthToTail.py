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
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k<=0:
            return None
        first = head 
        second = head
        i=0
        while i<k-1 and first.next!=None:
            first= first.next
            i+=1
        if i != k-1:
            return None
        while first.next!=None:
            first = first.next
            second = second.next
        return second 
