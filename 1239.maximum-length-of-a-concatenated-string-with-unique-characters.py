#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
from typing import List


class Solution:
    '''
    This is a DP problem
    1 <= arr.length <= 16, small enough to do it semi-brute force
    we can find for all possible combinations inside arr which do not have overlapping characters
    we use the dp array to keep all the possible used characters
    dp[i] = all possible sets of unique characters if we use arr[:i+1]    
    '''
    def maxLength(self, arr: List[str]) -> int:
        n, dp = len(arr), [set()]
        for string in arr:
            if len(set(string)) == len(string): # string is composed of unique characters
                for ele in dp[:]:
                    if not ele & set(string): # no overlap between element and the current string
                        dp.append( ele | set(string))
        return max(len(ele) for ele in dp)
# @lc code=end

