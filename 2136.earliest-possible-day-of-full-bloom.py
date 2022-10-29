#
# @lc app=leetcode id=2136 lang=python3
#
# [2136] Earliest Possible Day of Full Bloom
#

# @lc code=start
class Solution:
    # planting days cannot overlap
    # So the greedy strategy is to grow the long growtime plants first
    # Use the grow time in between to plant the shorter grow time ones
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        data = []
        for grow, plant in zip(growTime, plantTime):
            data.append([grow, plant])
        data.sort(key = lambda x: -x[0])
        result, plant_cumu = 0, 0
        for grow, plant in data:
            result = max(result, plant_cumu + grow + plant)
            plant_cumu += plant
        return result
# @lc code=end

