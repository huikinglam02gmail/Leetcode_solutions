#
# @lc app=leetcode id=2981 lang=python3
#
# [2981] Find Longest Special Substring That Occurs Thrice I
#

# @lc code=start
class Solution:
    def countSpecial(self, l, s):
        seen = {}
        result = [0] * 26
        for i in range(l): seen[s[i]] = seen.get(s[i], 0) + 1
        if len(seen) == 1: result[ord(list(seen.keys())[0]) - ord('a')] += 1
        for i in range(l, len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            seen[s[i - l]] -= 1
            if seen[s[i - l]] == 0: seen.pop(s[i - l])
            if len(seen) == 1: result[ord(list(seen.keys())[0]) - ord('a')] += 1
        return max(result)
    
    def maximumLength(self, s: str) -> int:
        l, r = 0, len(s)
        while l < r:
            mid = l + (r - l) // 2
            if self.countSpecial(mid, s) >= 3: l = mid + 1
            else: r = mid
        return l - 1 if l > 1 else -1
        
# @lc code=end

