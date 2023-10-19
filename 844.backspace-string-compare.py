#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_final = []
        for c in s:
            if c == '#':
                if s_final:
                    s_final.pop()
            else:
                s_final.append(c)
        t_final = []
        for c in t:
            if c == '#':
                if t_final:
                    t_final.pop()
            else:
                t_final.append(c)
        if len(s_final) != len(t_final):
            return False
        else:
            for i, j in zip(s_final, t_final):
                if i != j:
                    return False
            return True
# @lc code=end

