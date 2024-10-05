#
# @lc app=leetcode id=2211 lang=python3
#
# [2211] Count Collisions on a Road
#

# @lc code=start
class Solution:
    '''
    USe a stack to simulate
    '''
    def countCollisions(self, directions: str) -> int:
        result = 0
        cars = []
        for d in directions:
            temp = d
            if temp == "L" and cars and cars[-1] != "L":
                if cars.pop() == "R": result += 2
                else: result += 1
                temp = "S"
            while temp == "S" and cars and cars[-1] == "R":
                cars.pop()
                result += 1
            cars.append(temp)               
        return result


# @lc code=end

