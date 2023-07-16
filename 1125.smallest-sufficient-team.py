#
# @lc app=leetcode id=1125 lang=python3
#
# [1125] Smallest Sufficient Team
#

# @lc code=start
from typing import List


class Solution:
    '''
    DP problem
    1 <= req_skills.length <= 16
    Therefore we can use bitmask to represent the skill set
    dp[mask] = candidate lists of shortest sufficient team of the smallest possible size
    We start with a dictionary of only 0 as key
    We add people one by one into groups which will lead to shorter group or if there are not sufficient team previously
    '''

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_set, ns = {}, len(req_skills)
        for i, skill in enumerate(req_skills):
            skill_set[skill] = i
        dp = {0: []}
        for i, skills in enumerate(people):
            people_mask = 0
            for skill in skills:
                people_mask ^= (1<<skill_set[skill])
            for skill_mask, team in list(dp.items()):
                new_mask = skill_mask | people_mask
                if new_mask not in dp or len(dp[new_mask]) > 1 + len(team):
                    dp[new_mask] = team + [i]
        return dp[(1<<ns) - 1]
                
# @lc code=end

