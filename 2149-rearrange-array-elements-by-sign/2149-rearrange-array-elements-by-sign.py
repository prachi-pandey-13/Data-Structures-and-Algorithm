class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pos = []
        # neg = []
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] > 0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i])
        # for i in range(n):
        #     nums[2*i] = pos[i]
        #     nums[(2*i)+1] = neg[i]
        # return nums

        n = len(nums)
        result = [0]*n
        pos = 0
        neg = 1
        for i in range(n):
            if nums[i] > 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2
        return result