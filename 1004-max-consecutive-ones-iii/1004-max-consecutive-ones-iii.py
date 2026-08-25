class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # count = 0
        # n = len(nums)
        # for i in range(0, n):
        #     zeros = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             zeros += 1
        #         if zeros > k:
        #             break
        #         count = max(count, j-i+1)
        # return count

        n = len(nums)
        count = 0
        zeros = 0
        left = right = 0
        while right < n:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                count = max(count, right-left+1)
            right += 1
        return count