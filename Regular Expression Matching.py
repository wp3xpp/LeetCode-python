'''Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true'''
class Solution:  
    cache = {}  
    # @return a boolean  
    def isMatch(self, s, p):  
        if (s, p) in self.cache:  
            return self.cache[(s, p)]  
  
        if not p:  
            return not s  
  
        if len(p) == 1 or p[1] != '*':  
            self.cache[(s[1:], p[1:])] = self.isMatch(s[1:], p[1:])  
            return len(s) > 0 and (p[0] == '.' or s[0] == p[0]) and self.cache[(s[1:], p[1:])] 
        while s and (p[0] == '.' or s[0] == p[0]):  
            self.cache[(s, p[2:])] = self.isMatch(s, p[2:])  
            if self.cache[(s, p[2:])]:  
                return True  
            s = s[1:]  
        self.cache[(s, p[2:])] = self.isMatch(s, p[2:])  
        return self.cache[(s, p[2:])]