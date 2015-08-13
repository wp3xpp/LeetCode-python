# Determine whether an integer is a palindrome. Do this without extra space.
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        digit = 1
        while x/digit >= 10:
            digit *= 10
        while x:
            left = x / digit
            right = x % 10
            if left != right:
                return False
            x -= left * digit
            x /= 10
            digit /= 100
        return True

