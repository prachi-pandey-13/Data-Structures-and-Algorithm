class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s)
        # count = 0
        # for i in range(0,n):
        #     myset = set()
        #     for j in range(i, n):
        #         if s[j] in myset:
        #             break
        #         myset.add(s[j])
        #         count = max(count, j-i+1)
        # return count

        n = len(s)
        mydict = {}
        left, right = 0, 0
        count = 0
        while right < n:
            if s[right] in mydict:
                left = max(left, mydict[s[right]]+1) 
            mydict[s[right]] = right
            count = max(count, right-left+1)
            right += 1
        return count
