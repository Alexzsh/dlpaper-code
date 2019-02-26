#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if popV[0] not in pushV:
            return False
        a = pushV[0:pushV.index(popV[0])+1]
        b = pushV[pushV.index(popV[0])+1:]
        while len(popV) != 0 and (popV[0] in a or popV[0] in b):
            if len(a) != 0 and a[-1] == popV[0]:
                a.pop(-1)
                popV.pop(0)
            elif len(b) != 0 and b[0] == popV[0]:
                b.pop(0)
                popV.pop(0)
            elif len(b) != 0:
                a.append(b.pop(0))
            else:
                return False
        return True

if __name__ == '__main__':
    print(Solution().IsPopOrder([1,2,3,4,5],[3,5,4,2,1]))
