#
# @lc app=leetcode id=3034 lang=python3
#
# [3034] Number of Subarrays That Match a Pattern I
#

# @lc code=start
from typing import List


class Solution:
    '''
    Construct the transition array and count # of matching subarray by rolling hash
    '''
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        txt = ""
        pat = ""
        for num in pattern: pat += chr(ord('a') + num + 1)
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]: txt += 'c'
            elif nums[i + 1] == nums[i]: txt += 'b'
            else: txt += 'a'
        return len(self.search(pat, txt))

    '''
    Python program to search the pattern in given text 
    using KMP Algorithm
    '''
    def constructLps(self, pat):
        len_ = 0
        m = len(pat)
        lps = [0] * m
        i = 1
        while i < m:
            if pat[i] == pat[len_]:
                len_ += 1
                lps[i] = len_
                i += 1
            else:
                if len_ != 0: len_ = lps[len_ - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, pat, txt):
        n = len(txt)
        m = len(pat)
        res = []
        lps = self.constructLps(pat)

        i = 0
        j = 0

        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    res.append(i - j)
                    j = lps[j - 1]
            else:
                if j != 0: j = lps[j - 1]
                else: i += 1
        return res 
# @lc code=end

