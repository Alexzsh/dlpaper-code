# coding=utf-8
"""
@version=1.0
@author:zsh
@file:repeatNumInList.py
@time:2019/2/17 12:38
"""


def repeatNum1(numList):
    '''
    O(n),O(n)
    :param numList:
    :return:
    '''
    if len(numList) == 0:
        return
    if min(numList) < 0 or max(numList) > len(numList):
        return
    res = [0] * len(numList)
    resList = []
    for i in numList:
        if res[i] == 0:
            res[i] += 1
        else:
            resList.append(i)
    # resNum = [index for index,i in enumerate(res) if i>1]
    return resList


def repeatNum2(numList):
    '''
    O(n),O(1)
    :param numList:
    :return:
    '''
    if len(numList) == 0:
        return
    if min(numList) < 0 or max(numList) > len(numList):
        return
    resList = set()
    for index, i in enumerate(numList):
        while(numList[index] != index):
            if numList[index] == numList[i]:
                resList.add(numList[index])
                break
            temp = numList[index]
            numList[index] = numList[numList[index]]
            numList[temp] = temp
    return resList


def quick_sort(numList, left, right):
    '''
    O(nlog(n))
    :param numList:
    :return:
    '''
    # print(left,right)
    if left >= right:
        return
    low = left
    high = right
    key = numList[low]
    while left < right:
        while numList[right] > key and left < right:
            right -= 1
        numList[left]=numList[right]
        while numList[left] <= key and left < right:
            left += 1
        numList[right]=numList[left]

    numList[right]=key
    quick_sort(numList,low,left-1)
    quick_sort(numList,left+1,high)

def quick_sort1(numList,left,right):
    # print(left,right)
    if left<right:
        q=partiton(numList,left,right)
        quick_sort1(numList,left,q-1)
        quick_sort1(numList,q+1,right)
def partiton(numList,left,right):
    key = numList[right]
    j = left-1
    for i in range(left,right):
        if numList[i]<key:
            j+=1
            numList[j],numList[i]=numList[i],numList[j]
    numList[j+1],numList[right]=numList[right],numList[j+1]
    return j+1

if __name__ == '__main__':
    import numpy as np
    import time
    import matplotlib.pyplot as plt

    pltRes,pltRes1 = [],[]
    for i in range(1,11):

        res,res1=[],[]
        for j in range(3):
            li = np.random.randint(int(np.exp2(i)),size=int(np.exp2(i)))
            li1=li
            start = time.time()
            quick_sort1(li,0,len(li)-1)
            end = time.time()
            quick_sort(li1,0,len(li1)-1)
            end1=time.time()
            res1.append(end1-end)
            res.append(end-start)
        pltRes.append(np.average(res))
        pltRes1.append(np.average(res1))

        print(i,np.average(res),np.average(res1))
    plt.figure()
    plt.plot(range(1, 11), np.array(pltRes), 'bo')
    plt.plot(range(1, 11), np.array(pltRes1), '--')

    plt.show()
    # li=[21,3,1,4,23]
    # quick_sort(li, 0, len(li) - 1)
    # print(li)