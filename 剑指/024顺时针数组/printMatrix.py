#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:
# -*- coding:utf-8 -*-
import copy
class Solution:
    
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here1

        cols = len(matrix[0])
        rows = len(matrix)

        resCols = [[0]*cols]
        res = copy.deepcopy(matrix)
        
        resCol,resRow,item = 0,0,0
        
        tempRow,tempCol=rows,cols
        circle=1
        sumNum=0
        for i in range(tempRow):
            for j in range(tempCol):
                res[resRow][resCol] = matrix[i][j]
                sumNum += 1
                if sumNum<cols:
                    resCol+=1
                elif sumNum>=cols and sumNum<cols+rows-1:
                    resRow+=1
                elif sumNum>=cols+rows-1 and sumNum<2*(cols)+rows-2:
                    resCol-=1
                else:
                    resRow-=1
                
                
                if sumNum==2*(rows-1+cols-1):
                    cols-=2
                    rows-=2
                    sumNum=0
                    resRow += 1
                    resCol+=1
        print(res)
        return res
                
if __name__ == '__main__':
    matrix=[[1,2,3,4,17],[5,6,7,8,18],[9,10,11,12,19],[13,14,15,16,20]]
    print(matrix)
    Solution().printMatrix(matrix)
    
