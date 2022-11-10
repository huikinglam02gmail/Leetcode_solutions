#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    # Elementary use of stacks
    def removeDuplicates(self, s: str) -> str:
        result = []
        for c in s:
            if result and result[-1] == c:
                result.pop()
            else:
                result.append(c)
        return "".join(result)
# @lc code=end

