#
# @lc app=leetcode id=1781 lang=python3
#
# [1781] Sum of Beauty of All Substrings
#

# @lc code=start
class Solution:
    '''
    From s[i], we can expand to count the most and least frequent characters within s[i:j]. each check is O(26), so time complexity is O(26 * n * n)
    '''
    def beautySum(self, s: str) -> int:
        result, n = 0, len(s)
        for i in range(n):
            count = [0] * 26
            for j in range(i, n):
                count[ord(s[j]) - ord('a')] += 1
                result += max(count) - min([c for c in count if c > 0])
        return result
# @lc code=end

