'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ¡Ü b ¡Ü c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        res = []
        length=len(nums)
        if length<3:return res
        nums.sort()
        for i in range(length):
            if nums[i]>0:break
            if i>0 and nums[i]==nums[i-1]:continue
            begin=i+1;end=length-1
            while begin < end:
                sum=nums[i]+nums[begin]+nums[end]
                if sum==0:
                    tmp=[nums[i],nums[begin],nums[end]]
                    res.append(tmp)
                    begin+=1;end-=1
                    while begin<end and nums[begin]==nums[begin-1]:begin+=1
                    while begin<end and nums[end] == nums[end+1]:end-=1
                elif sum>0:end-=1
                else:begin+=1
        return res
        
