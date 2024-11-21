#
# @lc app=leetcode id=2410 lang=python3
#
# [2410] Maximum Matching of Players With Trainers
#

# @lc code=start
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, result = 0, 0
        for trainer in trainers:
            if i < len(players) and players[i] <= trainer:
                i += 1
                result += 1
        return result
# @lc code=end

