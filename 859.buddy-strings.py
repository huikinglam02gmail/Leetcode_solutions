#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    '''
    Two cases to be a pair of buddy strings:
    identical, at least one character appears twice
    Two mismatches, corresponding positions    
    '''

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) == len(goal):
            hash_table = {}
            mismatch = []
            for i in range(len(s)):
                hash_table[s[i]] = hash_table.get(s[i], 0) + 1
                if s[i] != goal[i]:
                    mismatch.append([s[i], goal[i]])
            if len(mismatch) == 0:
                return max(hash_table.values()) > 1
            elif len(mismatch) == 1:
                return False
            elif len(mismatch) == 2:
                return mismatch[0][0] == mismatch[1][1] and mismatch[0][1] == mismatch[1][0]
        return False
# @lc code=end

