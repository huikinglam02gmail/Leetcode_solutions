#
# @lc app=leetcode id=1585 lang=python3
#
# [1585] Check If String Is Transformable With Substring Sort Operations
#

# @lc code=start
class Solution:
    # First note that we cannot actively move a character to its right
    # When we move a character to the left, we can do so if
    # there are no elements smaller than itself on its left
    # The question is only asking for if it's possible, not the optimal path
    # Our strategy will be like this:
    # First record all appearance of of each digit
    # Then for each character in t
    # Ask if the appearance of smaller digits is always later than itself. 
    def isTransformable(self, s: str, t: str) -> bool:
        appearance = [[] for i in range(10)]
        seenInT = [0]*10
        for i, c in enumerate(s):
            appearance[int(c)].append(i)
        for c in t:
            if seenInT[int(c)] >= len(appearance[int(c)]):
                return False
            for i in range(int(c)):
                if seenInT[i] < len(appearance[i]) and appearance[i][seenInT[i]] < appearance[int(c)][seenInT[int(c)]]:
                    return False
            seenInT[int(c)] += 1
        return True
# @lc code=end

