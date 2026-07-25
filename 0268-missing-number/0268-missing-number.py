class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        add = (n*(n+1))//2
        sum_n = sum(nums)
        return add - sum_n