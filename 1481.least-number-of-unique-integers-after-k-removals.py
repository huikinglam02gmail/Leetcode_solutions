#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
class Solution:
    # Remove the numbers with less occurrence first
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        occur = {}
        for num in arr:
            if num not in occur:
                occur[num] = 0
            occur[num] += 1
        kvp = list(occur.items())
        kvp.sort(key = lambda x: x[1])
        n = len(kvp)
        i = 0
        while k > 0:
            if kvp[i][1] <= k:
                k -= kvp[i][1]
                i += 1
            else:
                k = 0
        return n - i
# @lc code=end

