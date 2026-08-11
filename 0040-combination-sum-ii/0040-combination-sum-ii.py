class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(index, total, subset):
            if total == 0:
                result.append(subset.copy())
                return
            elif total < 0 or index >= len(candidates):
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                add = total - candidates[i]
                backtrack(i+1, add, subset)
                subset.pop()
        backtrack(0, target, [])
        return result
