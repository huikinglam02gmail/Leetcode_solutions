#
# @lc app=leetcode id=1638 lang=python3
#
# [1638] Count Substrings That Differ by One Character
#

# @lc code=start
class Solution:
    # 1 <= s.length, t.length <= 100
    # So can try all substrings of s
    # For each substring, ask if the count only differ by 1 by scanning through t
    def countSubstrings(self, s: str, t: str) -> int:
        n = len(s)
        result = 0
        for i in range(n - 1):
            hashS = [0]*26
            for j in range(i, n):
                hashS[ord(s[j]) - ord('a')] += 1
                hashT = [0]*26
                for k in range(len(t)):
                    hashT[ord(t[k]) - ord('a')] += 1
                    if k >= j - i + 1:
                        hashT[ord(t[k - j + i - 1]) - ord('a')] -= 1
                    if sum([abs(hashS[l] - hashT[l]) for l in range(26)]) == 2:
                        result += 1
        return result
        
# @lc code=end

