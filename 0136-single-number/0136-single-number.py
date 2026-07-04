class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = 0
        # for num in nums:
        #     result = result ^ num
        # return result
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for key in hashmap:
            if hashmap[key] == 1:
                return key