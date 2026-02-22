#
# @lc app=leetcode id=3842 lang=python3
#
# [3842] Toggle Light Bulbs
#

# @lc code=start
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()
        for bulb in bulbs:
            if bulb in on: on.remove(bulb)
            else: on.add(bulb)
        return sorted(list(on))
# @lc code=end

