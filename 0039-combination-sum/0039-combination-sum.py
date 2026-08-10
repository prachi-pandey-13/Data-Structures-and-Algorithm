class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def solve(index, total, subset):
            if total == target:
                result.append(subset.copy())
                return
            if total > target:
                return
            elif index >= len(candidates):
                return
            subset.append(candidates[index])
            add = total + candidates[index]
            solve(index, add, subset)
            subset.pop()
            add = total
            solve(index+1, add, subset)
        solve(0,0,[])
        return result