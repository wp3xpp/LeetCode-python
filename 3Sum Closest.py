'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
        	return sum(nums)
        nums.sort()
        length = len(nums)
        temp_goal = float('inf')
        for i in range(length):
        	left, right = i + 1, length - 1
        	while left < right:
        		goal = nums[left] + nums[i] + nums[right] - target
        		if abs(goal) <= temp_goal:
        			temp_goal = abs(goal)
        			res = nums[left] + nums[i] + nums[right]
        		if temp_goal > 0:
        			right -= 1
        		else:
        			left += 1
        		
        return res
