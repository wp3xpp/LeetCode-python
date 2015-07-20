# -*- coding: utf-8 -*-
'''
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.
'''

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
    	n = len(s)
    	beginIndex = 0
    	maxLength = 1
    	table = [[False for x in range(n)] for y in range(n)]
    	for i in range(n):
    		table[i][i] = True
    	for i in range(n-1):
    		if s[i] == s[i+1]:
    			table[i][i+1] = True
    			beginIndex = i
    			maxLength = 2
    	Len = 3
    	while Len <= n:
    		for i in range(n-Len-1):
    			j = i+Len-1
    			if(table[i+1][j-1] and s[i] == s[j]):
    				table[i][j] = True
    				beginIndex = i
    				maxLength = Len
    		Len += 1
    	return s[i:i+maxLength]
if __name__ == '__main__':
	t = Solution()
	print t.longestPalindrome('"lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges"')
