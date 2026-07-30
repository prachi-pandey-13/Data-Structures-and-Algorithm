class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # n = len(nums)
        # my_set = set()
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 temp.sort()
        #                 my_set.add(tuple(temp))
        # # return [list(ans) for ans in my_set]

        # n = len(nums)
        # result = set()
        # for i  in range(0,n):
        #     my_set = set()
        #     for j in range(i+1, n):
        #         third = -(nums[i] + nums[j])
        #         if third in my_set:
        #             temp = [nums[i], nums[j], third]
        #             temp.sort()
        #             result.add(tuple(temp))
        #         my_set.add(nums[j])
        # return [list(ans) for ans in result]

        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k] 
                if total == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    result.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return result
