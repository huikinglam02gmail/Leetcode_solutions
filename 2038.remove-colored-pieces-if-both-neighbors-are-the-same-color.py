#
# @lc app=leetcode id=2038 lang=python3
#
# [2038] Remove Colored Pieces if Both Neighbors are the Same Color
#

# @lc code=start
class Solution:
    '''
    As "ABBA" or "BAAB" means the end of the opportunities to take from colors, we cannot merge any two "A" separated by one or more "B"or otherwise. So the game is just about which one has more consecutive "A" or "B".
    '''
    def winnerOfGame(self, colors: str) -> bool:
        colors = "C" + colors + "C"
        count = [0] * 2
        consec = 0
        last = ""
        for color in colors:
            if color != last:
                if last == "A":
                    count[0] -= min(consec, 2)
                elif last == "B":
                    count[1] -= min(consec, 2)
                consec = 1
            else:
                consec += 1
            if color == "A":
                count[0] += 1
            elif color == "B":
                count[1] += 1
            last = color
        return count[0] > count[1]
# @lc code=end

