s = input().lower()
res = []
flag = False
res1 = -1
resc = '$'
if s.count(s[0]) == 1:
    print(s[0])
else:
    for index, i in enumerate(s):
        if s.count(i) == 1:
            res1 = index
            resc = i
            flag = True
            break
        if i not in res:
            res.append(i)

res.sort()
repeat = s.find(res[0])
if len(res) > 0:
    if res1!=-1:
        if res1 < repeat:
            print(resc)
        elif resc < res[0]:
            print(min(resc,res[0]))
    else:
        print(res[0])