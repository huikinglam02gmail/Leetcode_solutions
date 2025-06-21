#
# @lc app=leetcode id=3006 lang=python3
#
# [3006] Find Beautiful Indices in the Given Array I
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aFound = self.search(a, s)
        bFound = self.search(b, s)
        result = []
        for aIndex in aFound:
            leftIndex = bisect.bisect_left(bFound, aIndex - k)
            rightIndex = bisect.bisect_right(bFound, aIndex + k)
            if leftIndex < rightIndex: result.append(aIndex)
        return result
        
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

