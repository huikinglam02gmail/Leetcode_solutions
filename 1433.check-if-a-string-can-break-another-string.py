#
# @lc app=leetcode id=1433 lang=python3
#
# [1433] Check If a String Can Break Another String
#

# @lc code=start
class Solution:
    # This question is pretty simple
    # Sort s1 and s2
    # Check if s1[i] <= s2[i] or s2[i] <= s1[i] for all i
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted([c for c in s1]))
        s2 = ''.join(sorted([c for c in s2]))
        return all([s1[i] >= s2[i] for i in range(len(s1))]) or all([s1[i] <= s2[i] for i in range(len(s1))])
        
# @lc code=end

