class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
    	if strs == [] or strs == ['']:
    		return ""
    	prefix = ""
    	i = 0
    	flag = True
    	while flag:
    		for s in strs:
    			if len(s)-1 < i or s[i] != strs[0][i]:
    				flag = False
    				break
    		prefix += strs[0][i] if flag else ''
    		i += 1
    	return prefix