class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse(nums, left, right):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-k-1)
        reverse(nums, 0, n-1)


        # n = len(nums)
        # rotations = k % n
        # for i in range(0, rotations):
        #     e = nums.pop()
        #     nums.insert(0, e)
        #     # nums[:] = [nums[-1]] + nums[0:n-1]
        # return nums 
        
        # n = len(nums)
        # nums[:] = nums[n-k:] + nums[:n-k]
        # return nums