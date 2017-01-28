class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        new_nums = [0]*num_len
        if (k<0):
            k = (k % num_len) + num_len
        for i in range(num_len):
            new_nums[(i+k) % num_len] = nums[i]
        for i in range(num_len):
            nums[i] = new_nums[i]
