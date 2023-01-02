#
# @lc app=leetcode id=1585 lang=python3
#
# [1585] Check If String Is Transformable With Substring Sort Operations
#

# @lc code=start
class Solution:
    # We should note that we cannot move a character to its right actively
    # And when we move a character to the left, we can do so if there are no 
    # The question is only asking for if it's possible, not the optimal path
    # So for each digit in t (t[i]), we find the corresponding position in s s[j]
    # If i > j, we ask if s[k] > s[i] for all j <= k < i
    # In other words, we can check for digit < s[i], and make sure there are no entries between i and j
    def isTransformable(self, s: str, t: str) -> bool:
        
# @lc code=end

