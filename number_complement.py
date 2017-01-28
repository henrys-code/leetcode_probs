"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        shift = 0
        while (num < 2**31):
            num = num << 1
            shift += 1
        num = num ^ 0xFFFFFFFF
        return num >> shift
