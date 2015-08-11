# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.strip()
        if str == '0' or str == '' :
            return 0
        if len(str) > 1:
            if str[0] == '-' or str[0] == '+':
                if ord(str[1]) < ord('0') or ord(str[1]) > ord('9'):
                    return 0
        flag = True
        if str[0] == '-':
            flag = False
            str = str[1:]
        if str[0] == '+':
            str = str[1:]
        res = 0
        for i in str:
            if ord(i) < ord('0') or ord(i) > ord('9'):
                break
            res = res * 10 + (ord(i) - ord('0'))
        res = res if flag else -res
        if res > 0x7fffffff:
            return 0x7fffffff
        if res < -0x80000000:
            return -0x80000000
        return res
        
if __name__ == '__main__':
	s = Solution()
	print s.myAtoi('1')


