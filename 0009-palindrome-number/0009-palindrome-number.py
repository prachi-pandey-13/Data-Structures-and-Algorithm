class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        original = x
        while x != 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        return original == rev