s = input().lower()
res=[s]
notRepeat = []
while len(res)>0:
    temp = res.pop(0)
    flag = False
    for i in set(list(temp)):
        counts = temp.count(i)
        if counts==2:
            flag = True
            start = 0
            for j in range(2):
                if j==0:
                    index = temp.find(i)
                else:
                    index = temp.rfind(i)
                if index!=len(temp)-1:
                    start = index+1
                    res.append(temp[:index]+temp[index+1:])
                else:
                    res.append(temp[:index])
    if not flag:
        notRepeat.append(temp)
notRepeat.sort(key=str.lower)
print(notRepeat[0][0])
