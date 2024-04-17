#
# @lc app=leetcode id=3114 lang=python3
#
# [3114] Latest Time You Can Obtain After Replacing Characters
#

# @lc code=start
class Solution:
    '''
    Generate all possible times
    Try to match
    '''
    def __init__(self):
        self.result = []
        for i in range(719, -1, -1): self.result.append(str(i // 60).zfill(2) + ":" +  str(i % 60).zfill(2))

    def findLatestTime(self, s: str) -> str:
        for t in self.result:
            if (s[0] == "?" or s[0] == t[0]) and (s[1] == "?" or s[1] == t[1]) and (s[3] == "?" or s[3] == t[3]) and (s[4] == "?" or s[4] == t[4]): return t
        return ""
# @lc code=end

