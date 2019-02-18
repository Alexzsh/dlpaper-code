
def findNum(numList,row,col,num):
    flag = False
    rowPviot,colPviot=0,col-1
    while rowPviot<=row and colPviot>=0:
        if numList[rowPviot*col+colPviot] == num:
            flag = True
            break
        elif numList[rowPviot*col+colPviot] > num:
            colPviot -= 1
        else:
            rowPviot += 1
    return flag


if __name__ == "__main__":
    li = [1,2,8,9,2,4,9,12,4,7,10,13,6,8,11,15]
    print(findNum(li,4,4,5))
