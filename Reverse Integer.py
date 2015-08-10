# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flag = True
        if x == 0 :
            return 0
        if x < 0:
            flag = False
        x = abs(x)
        res = ""
        for i in str(x):
            res = i + res
        while res[0] == '0':
            res = res[1:]
        res = int(res) if flag else -int(res)
        if res > 2147483647 or res < -2147483648:
        	return 0
        return res

if __name__ == '__main__':
	s = Solution()
	print s.reverse(-56789)

