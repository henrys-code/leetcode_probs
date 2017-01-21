"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        even = {}
        odd = {}
        for i in s:
            dict[i] = dict[i] + 1 if i in dict.keys() else 1
        for i in dict.keys():
            if dict[i] % 2 == 0: even[i] = dict[i]
            if dict[i] % 2 != 0:  odd[i] = dict[i]
        ret = sum(even.values()) + sum(odd.values()) - len(odd.values())
        return ret if len(odd.keys()) == 0 else ret + 1
