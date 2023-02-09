#
# @lc app=leetcode id=2306 lang=python3
#
# [2306] Naming a Company
#

# @lc code=start
from typing import List


class Solution:
    # Group ideas according to first letter
    # To form a valid name, it must be "a" + "cde" "b" + "fgh"
    # So for each pair of first letter charaters, it is the product of exclusive parts of each pair times 2
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for i in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].add(idea[1:])
        
        result = 0
        for i in range(25):
            for j in range(i + 1, 26):
                l = len(groups[i].intersection(groups[j]))
                result += 2*(len(groups[i]) - l)*(len(groups[j]) - l)
        return result
# @lc code=end

