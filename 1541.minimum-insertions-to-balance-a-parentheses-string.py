#
# @lc app=leetcode id=1541 lang=python3
#
# [1541] Minimum Insertions to Balance a Parentheses String
#

# @lc code=start
class Solution:
    # replace '))' with '}'
    def minInsertions(self, s: str) -> int:
        openBracket = 0
        result = 0
        s = s.replace("))",'}')
        for c in s:
            if c == '(':
                openBracket += 1
            elif c == '}':
                if openBracket > 0:
                    openBracket -= 1
                else:
                    result += 1
            else:
                if openBracket > 0:
                    openBracket -= 1
                    result += 1
                else:
                    result += 2
        return result + openBracket*2
# @lc code=end

