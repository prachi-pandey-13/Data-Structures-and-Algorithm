class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        maximum = 0
        leftsum = 0
        rightsum = 0
        if n == k:
            return sum(cardPoints)
        for i in range(0, k):
            leftsum += cardPoints[i]
        maximum = leftsum
        rightind = n-1
        for i in range(k-1, -1, -1):
            leftsum -= cardPoints[i]
            rightsum += cardPoints[rightind]
            maximum = max(maximum, leftsum + rightsum)
            rightind -= 1
        return maximum
