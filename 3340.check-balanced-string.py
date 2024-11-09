#
# @lc app=leetcode id=3340 lang=python3
#
# [3340] Check Balanced String
#

# @lc code=start
class Solution:
    def isBalanced(self, num: str) -> bool:
        odd, even = 0, 0
        for i in range(len(num)):
            if i % 2: odd += int(num[i])
            else: even += int(num[i])
        return odd == even
# @lc code=end

