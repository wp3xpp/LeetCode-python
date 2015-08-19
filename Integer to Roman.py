'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]   
        value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        res = ""
        while num > 0 :
            while num >= value[i]:
                num -= value[i]
                res += symbol[i]
                print num
            i += 1
        return res

if __name__ == "__main__":
    s = Solution()
    print s.intToRoman(2434)
