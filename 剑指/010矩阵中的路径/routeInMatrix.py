#-*- coding:utf-8 -*-
#author: zsh
#modified by zsh at date
#version:
#history:
#relate on:

# -*- coding:utf-8 -*-


class Solution(object):
    direct=[(0,-1),(0,1),(-1,0),(1,0)]
    @classmethod
    def hasPath(cls,matrix, rows, cols, path):
        # write code here
        if len(matrix) == 0 or rows == 0 or cols == 0 or len(path)==0:
            return False

        visited = [False]*len(matrix)

        for i in range(rows):
            for j in range(cols):
                if cls.hasPathVisited(cls,matrix, rows, cols, i, j, path, visited):
                    return True

        return False
    
    def hasPathVisited(self, matrix, rows, cols, row, col, path, visited):
        current = row*cols+col
        if len(path) == 0:
            return True
        hasPath = False
        if (row>=0 and row<=rows-1) and (col>=0 and col<=cols-1) and not visited[current] and matrix[current]==path[0]:
            visited[current]=True
            for i in range(4):
                hasPath |= self.hasPathVisited(
                    self,
                    matrix, rows, cols, row+self.direct[i][0], col+self.direct[i][1], path[1:], visited)
            if not hasPath:
                visited[current]=False
        return hasPath
    
if __name__ == '__main__':
    print(Solution.hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))
