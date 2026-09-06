class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex = 0
        n = len(nums)
        for i in range(0, n):
            if i > maxindex:
                return False
            maxindex = max(maxindex, i + nums[i])
        return True