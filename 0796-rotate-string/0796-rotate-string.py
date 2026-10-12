class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        char_s = s
        n = len(s)
        for ch in char_s:
            if char_s == goal:
                return True
            char_s = char_s[-1] + char_s[:-1]
        return False