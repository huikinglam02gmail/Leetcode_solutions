#
# @lc app=leetcode id=2899 lang=python3
#
# [2899] Last Visited Integers
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use array to keep seen, but we have to count the indices backward
    '''
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        k = 0
        seen, ans = [], []
        for num in nums:
            if num > 0: 
                seen.append(num)
                k = 0
            else:
                k += 1
                n = len(seen)
                if k <= n: ans.append(seen[n - k])
                else: ans.append(num)
        return ans
        
# @lc code=end

