##Given an array of integers, find two numbers such that they add up to a specific target number.
##
##The function twoSum should return indices of the two numbers such that they add up to the target,
##where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
##
##You may assume that each input would have exactly one solution.
##
##Input: numbers={2, 7, 11, 15}, target=9
##Output: index1=1, index2=2
def twoSum(nums, target):
        i = 0
        j = len(nums) - 1
        t_nums = sorted(nums)
        while t_nums[i] + t_nums[j] != target:
            if t_nums[i] + t_nums[j] < target:
                i += 1
            else:
                j -= 1
        r_a = nums.index(t_nums[i])+1
        if t_nums[i] == t_nums[j]:
               nums[nums.index(t_nums[i])] = -1
        r_b = nums.index(t_nums[j])+1
        print r_a,r_b
        return sorted([r_a, r_b])
if __name__ == '__main__':
    nums = [3,2,4]
    print twoSum(nums, 6)
    print nums
