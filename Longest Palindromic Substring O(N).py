# -*- coding: utf-8 -*-
'''
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.
'''

class Solution:
    # @param {string} s
    # @return {string}
    def preProcess(self, s):
    	n = len(s)
    	if n == 0:
    		return "^$"
    	ret = "^"
    	for i in range(n):
    		ret += "#" + s[i:i+1]
    	ret += "#$"
    	return ret
    def longestPalindrome(self, s):
    	T = self.preProcess(s)
    	n = len(T)
    	P = [0 for i in range(n)]
    	C = 0
    	R = 0
    	for i in range(1, n-1):
    		i_mirror = 2*C-i
    		P[i] = min(R-i,P[i_mirror]) if R>i else 0
    		while(T[i+1+P[i]] == T[i-1-P[i]]):
    			P[i] += 1
    		if i+P[i] > R:
    			C = i
    			R = i + P[i]
    	maxLen = 0
    	centerIndex = 0
    	for i in range(1,n-1):
    		if P[i] > maxLen:
    			maxLen = P[i]
    			centerIndex = i
    	return s[(centerIndex-1-maxLen)/2: (centerIndex-1-maxLen)/2+maxLen]