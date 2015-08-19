'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]   
        value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        num = 0
        i = 0
        while s != '':
            while s.startswith(symbol[i]):
                num += value[i]
                s = s[len(symbol[i]):]
            i += 1
        return num

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('MMCDXXXIV')
            
