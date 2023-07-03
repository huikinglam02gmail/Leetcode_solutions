#
# @lc app=leetcode id=1787 lang=python3
#
# [1787] Make the XOR of All Segments Equal to Zero
#

# @lc code=start
from typing import List


class Solution:
    '''
    For all segments (subarray of size k) with XOR = j, it means nums[i] == nums[i + k]. Therefore we should record the occurences of nums[i], nums[i + k], ... etc, and put them as in a dictionary list of size k
    Then the question becomes, in each group, which number should I choose to represent the group. Notice it is possible that among the existing numbers, we cannot reach at total XOR of 0, as in example 3.
    Given we chose num_1... num_k, what if they do not XOR together to 0? So we find the group j in which occur[j][num_j] is minimum among different groups. This group we can all replace by 0^num_1^...^num_(j - 1)^num_(j + 1)^...^num_k.
    How about the case in Example 1 & 2, we can choose the final number from the given groups? Then we DP on the groups:
    dp[j][XS] = after considering groups[:j + 1], what are the number of elements within groups[:j + 1] that would contribute to final XOR sum of XS. We are looking for dp[n - 1][0]
    '''
    def minChanges(self, nums: List[int], k: int) -> int:
        occur = [{} for i in range(k)]
        n = len(nums)
        for i in range(n):
            occur[i % k][nums[i]] = occur[i % k].get(nums[i], 0) + 1
        
        dp = occur[0]
        for i in range(1, k):
            dpNew = {}
            for k, v in occur[i].items():
                for k1, v1 in dp.items():
                    dpNew[k1 ^ k] = max(dpNew.get(k1 ^ k, 0), v + v1)
            dp = dpNew
        
        return n - max(dp.get(0, 0), sum([max(o.values()) for o in occur]) - min([max(o.values()) for o in occur]))
# @lc code=end
