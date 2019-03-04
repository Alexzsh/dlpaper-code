# -*- coding:utf-8 -*-
class Solution(object):
    def Permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums)==0:
            return []
        res = []
        self.dfs(nums, res, '')
        return sorted(list(set(res)))
        
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + nums[i])