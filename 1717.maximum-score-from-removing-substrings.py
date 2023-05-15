#
# @lc app=leetcode id=1717 lang=python3
#
# [1717] Maximum Score From Removing Substrings
#

# @lc code=start
class Solution:
    '''
    Proof by contradiction:
    Assume score(ab) > score(ba) but removing ba first is optimal. This could only happen when the removal of a single ab prevents 2 ba removals, and score(remove ba first) > score(remove ab first) i.e. score(ba) * 2 > score(ab).
    Only b(ab)a satisfies this requirement. But after removing ab we can remove one ba, so we get score(ab) + score(ba) which is greater than score(ba) * 2. Thus removing ba first is not optimal, the assumption is wrong.
    So just decide which one to remove first, then remove the other. use stack to achieve so
    '''
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            order = ["ab", "ba"]
            score = [x, y]
        else:
            order = ["ba", "ab"]
            score = [y, x]
        stack1 = [c for c in s]
        stack2 = []
        result = 0
        for i in range(2):
            for c in stack1:
                if stack2 and stack2[-1] == order[i][0] and c == order[i][1]:
                    stack2.pop()
                    result += score[i]
                else:
                    stack2.append(c)
            stack1 = stack2.copy()
            stack2.clear()
        return result
        
            
# @lc code=end

