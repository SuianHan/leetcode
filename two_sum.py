class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            sub_num = target - num
            if sub_num in nums:
                t_index = nums.index(sub_num)
                if t_index != i:
                    return [i, t_index]