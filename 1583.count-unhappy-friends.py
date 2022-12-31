#
# @lc app=leetcode id=1583 lang=python3
#
# [1583] Count Unhappy Friends
#

# @lc code=start
from typing import List


class Solution:
    # Save the preferences in a preference matrix: Preference[i][j] = index
    # Then for each pair, record partner of each person
    # If partner[i] = k and partner[j] = l
    # Then we loop through all i, j pairs in which j != partner[i] and check for 2 conditions:
    # 1. Preference[i][j] < Preference[i][k]
    # 2. Preference[j][i] < Preference[j][l]
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        Preferences = [[-1 for i in range(n)] for j in range(n)]
        Partners = [-1]*n
        for u, v in pairs:
            Partners[u] = v
            Partners[v] = u
        for i, preference in enumerate(preferences):
            for j, num in enumerate(preference):
                Preferences[i][num] = j
        result = 0
        for i in range(n):
            for j in range(n):
                if j != Partners[i] and i != j:
                    k = Partners[i]
                    l = Partners[j]
                    if Preferences[i][j] < Preferences[i][k] and Preferences[j][i] < Preferences[j][l]:
                        result += 1
                        break
        return result


# @lc code=end

