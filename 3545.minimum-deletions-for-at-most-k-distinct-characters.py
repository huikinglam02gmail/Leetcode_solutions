#
# @lc app=leetcode id=3545 lang=python3
#
# [3545] Minimum Deletions for At Most K Distinct Characters
#

# @lc code=start
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count =[0] * 26
        for c in s: count[ord(c) - ord('a')] += 1
        count.sort(reverse=True)
        while count and count[-1] == 0: count.pop()
        return sum(count[k:]) if len(count) > k else 0
# @lc code=end

