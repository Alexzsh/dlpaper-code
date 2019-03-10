#coding=utf-8
"""
@version=1.0
@author:zsh
@file:2-1.py
@time:2019/3/10 17:33
"""
def func():
    s = input().lower()
    res = []
    res1 = -1
    resc = '$'
    if s.count(s[0]) == 1:
        print(s[0])
    else:
        for index, i in enumerate(s):
            if s.count(i) == 1:
                res1 = index
                resc = i
                break
            if i not in res:
                res.append(i)

        res.sort()
        repeat = s.find(res[0])
        if res1 != -1:
            if res1 < repeat:
                print(resc)
            elif s.rfind(res[0])<res1:
                print(res[0])
            else:
                start = s[0]
                for index,i in enumerate(s[1:repeat]):
                    if i==start:
                        print(i)
                        break
                    else:
                        print(min(resc, res[0]))
        else:
            print(res[0])
while True:
    func()