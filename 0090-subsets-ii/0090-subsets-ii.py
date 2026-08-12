class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def solve(index, subset):
            result.append(subset.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                solve(i+1, subset)
                subset.pop()
        solve(0, [])
        return result