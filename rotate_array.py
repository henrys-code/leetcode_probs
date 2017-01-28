class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        nums[:] = nums[-k % nums_len:] + nums[:-k % nums_len]
