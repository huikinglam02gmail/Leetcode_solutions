#
# @lc app=leetcode id=2195 lang=python3
#
# [2195] Append K Integers With Minimal Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= k <= 10 ^ 8, so don't try to sort and use two pointers to fill in one by one.
    Instead we assume the k list we put in is [1, 2, 3, .. , k]
    We separate out numbers which are <= k and > k. Put nums > k in a set
    Then for all 1 <= num <= k in nums, we increment nxt possible insertion by 1 and check against the > k set
    Also if 1 <= num <= k occured more than once, the whole list from num <= k 
    '''
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = k * (k + 1) // 2
        largerThanK = set([num for num in nums if num > k])
        nxt = k + 1
        while nxt in largerThanK: nxt += 1
        seen = set()
        for num in nums:
            if 1 <= num <= k: 
                if num not in seen:
                    result += nxt
                    result -= num
                    nxt += 1
                seen.add(num)
                while nxt in largerThanK: nxt += 1
        return result

# @lc code=end
