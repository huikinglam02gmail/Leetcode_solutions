#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
import collections


class Solution:
    '''
    # First count occurence of characters in t
    # Then for each index j, ask if s[i:j + 1] satisfy the substring requirement
    # need[c] can become negative, which means we have excess of the current character or it does not appear in t
    # missing = number of not yet appeared characters that is present in t
    '''
    def minWindow(self, s: str, t: str) -> str:
        need, missing, i, I, J = collections.Counter(t), len(t), 0, -1, -1
        for j, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if J == -1 or j - i <= J - I:
                    I, J = i, j
        if missing == 0:
            return s[I:J+1]
        else:
            return ""
# @lc code=end

