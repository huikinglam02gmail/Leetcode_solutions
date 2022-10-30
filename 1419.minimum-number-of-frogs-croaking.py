#
# @lc app=leetcode id=1419 lang=python3
#
# [1419] Minimum Number of Frogs Croaking
#

# @lc code=start
class Solution:
    # First go through the string to ensure croak appears equal number of times
    # Also at any time, the occurrences of croak should be nonincreasing
    # Then we can simulate the process to match each character
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        occur = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        for c in croakOfFrogs:
            occur[c] += 1
            if occur['c'] < occur['r'] or occur['r'] < occur['o'] or occur['o'] < occur['a'] or occur['a'] < occur['k']:
                return -1
        if occur['c'] != occur['r'] or occur['c'] != occur['o'] or occur['c'] != occur['a'] or occur['c'] != occur['k']:
            return -1
        
        frogs = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        prev_char = {'c': 'k', 'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        result = 0
        for c in croakOfFrogs:
            if frogs[prev_char[c]] > 0:
                frogs[prev_char[c]] -= 1
            else:
                result += 1
            frogs[c] += 1
        return result
# @lc code=end

