class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split()
        # words.reverse()
        # result = " ".join(words)
        # return result

        words = s.split()
        n = len(words)
        result = []
        for i in range(n-1, -1, -1):
            result.append(words[i])
            if i != 0:
                result.append(" ")
        return "".join(result)
