class Solution: #思路一:用一个TempString保存当前无重复字串 100ms
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        MaxLength = 0
        TempString = ""
        for i in s:
            if i not in TempString:
                TempString += i
                if len(TempString) > MaxLength:
                    MaxLength = len(TempString)
            else:
                TempString = TempString[TempString.index(i)+1:] + i
        return MaxLength
class Solution: #思路2:用hashtable保存下标，若重复则更新idx 112ms
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        MaxLength = 0
        Locs = {}
        idx = -1 #idx保存当前字串起始位置
        for i in range(len(s)):
            if Locs.get(s[i]) > idx:
                idx = Locs.get(s[i])
            if i-idx > MaxLength:
                MaxLength = i - idx
            Locs[s[i]] = i
        return MaxLength
