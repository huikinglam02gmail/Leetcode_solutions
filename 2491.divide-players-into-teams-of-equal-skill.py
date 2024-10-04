#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#

# @lc code=start
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2: return skill[0]*skill[1]
        S = sum(skill)
        if S % (n // 2) != 0: return -1
        else:
            target = S // (n // 2)
            skill.sort()
            i, j = 0, len(skill) - 1
            chemistry = 0
            while i < j:
                if skill[i] + skill[j] == target:
                    chemistry += skill[i] * skill[j]
                    i += 1
                    j -= 1
                else:
                    return -1
            return chemistry
# @lc code=end

