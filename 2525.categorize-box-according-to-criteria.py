#
# @lc app=leetcode id=2525 lang=python3
#
# [2525] Categorize Box According to Criteria
#

# @lc code=start
class Solution:
    '''
    Set bulky and heavy as bools
    '''
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 1000000000
        heavy = mass >= 100
        if bulky and heavy : return "Both"
        elif bulky: return "Bulky"
        elif heavy: return "Heavy"
        else: return "Neither"
# @lc code=end

