'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''


class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
    	n = len(s)
    	if n < numRows:
    		return s
    	newStr = ""
    	for i in range(numRows):
            j = i
            flag = True
            while j < n:
        		newStr += s[j]
        		if (i == 0) or (i == numRows-1):
        			j += 2 * (numRows-1)
        		else:
        			if(flag):
        				j += 2 * (numRows-i-1)
        				flag = False
        			else:
        				j += 2 * i
        				
        				flag = True
        return newStr
		

    			
    		
