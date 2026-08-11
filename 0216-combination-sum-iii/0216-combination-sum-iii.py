class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(last, total, subset):
            if total == n and len(subset) == k:
                result.append(subset.copy())
            elif total > n or len(subset) > k:
                return
            for i in range(last,10):
                add = total + i
                subset.append(i)
                backtrack(i+1, add, subset)
                subset.pop()
        backtrack(1,0,[])
        return result