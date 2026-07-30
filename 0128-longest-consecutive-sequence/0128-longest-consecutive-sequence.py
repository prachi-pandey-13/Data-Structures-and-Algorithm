class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # max_count = 0
        # for i in range(n):
        #     num = nums[i]
        #     count = 1
        #     while num+1 in nums:
        #         count += 1
        #         num = num+1
        #     max_count = max(max_count, count)
        # return max_count

        # n = len(nums)
        # nums.sort()
        # last_smaller = float("-inf")
        # longest = 0
        # for i in range(0,n):
        #     num = nums[i]
        #     if num-1 == last_smaller:
        #         count += 1
        #         last_smaller = num
        #     elif num != last_smaller:
        #         count = 1
        #         last_smaller = num
        #     longest = max(longest, count)
        # return longest

        n = len(nums)
        my_set = set()
        longest = 0
        for i in range(0,n):
            my_set.add(nums[i])
        for num in my_set:
            if num-1 not in my_set:
                st = num
                count = 1
                while st+1 in my_set:
                    count += 1
                    st += 1
                longest = max(longest, count)
        return longest




        