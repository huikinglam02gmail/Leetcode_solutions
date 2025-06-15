#
# @lc app=leetcode id=1432 lang=python3
#
# [1432] Max Difference You Can Get From Changing an Integer
#

# @lc code=start


class Solution:
    def maxDiff(self, num: int) -> int:
        maxSoFar = - float('inf')
        minSoFar = float('inf')
        s = str(num)
        for i in range(10):
            for j in range(10):
                if i == j or (int(s[0]) == i and j == 0): continue
                current = ""
                for c in s:
                    if c == str(i): current += str(j)
                    else: current += c
                maxSoFar = max(maxSoFar, int(current))
                minSoFar = min(minSoFar, int(current))
        return maxSoFar - minSoFar
                
# @lc code=end

