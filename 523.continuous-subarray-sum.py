#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    calculate prefix sum of nums
    idea: if (prefix[j] - prefix[i]) % k = 0, prefix[j] % k = prefix[i] % k
    Keep a hash table keeping prefix[i] % k and the index
    The number 0 needs to be treated as a special case     
    '''
   
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total, mod_hash = 0, {}
        for i, num in enumerate(nums):
            total += num
            modulo = total % k
            if i > 0 and modulo == 0: return True
            if modulo not in mod_hash: 
                mod_hash[modulo] =  i
            else:
                j = mod_hash[modulo]
                if i > j + 1 or nums[j] == 0:  return True
        return False
# @lc code=end

