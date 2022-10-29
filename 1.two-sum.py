#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for k,v in enumerate(nums):
            hash_map[v] = k
        for k,v in enumerate(nums):
            if target - v in hash_map:
                index = hash_map[target - v]
                if k != index:
                    return [k ,index]
        return [-1,-1]
# @lc code=end

