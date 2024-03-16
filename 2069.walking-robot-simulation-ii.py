#
# @lc app=leetcode id=2069 lang=python3
#
# [2069] Walking Robot Simulation II
#

# @lc code=start
from typing import List


class Robot:
    '''
    save x and y
    '''

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0
        self.dirs =  [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.dirNames = ["East", "North", "West", "South"]
        self.walked = False

    def step(self, num: int) -> None:
        num %= 2 * (self.w + self.h - 2)
        self.walked = True
        for i in range(num):
            if not (0 <= self.x + self.dirs[self.dir][0] < self.w and 0 <= self.y + self.dirs[self.dir][1] < self.h):
                self.dir += 1
                self.dir %= 4
            self.x += self.dirs[self.dir][0]
            self.y += self.dirs[self.dir][1]

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.x == 0 and self.y == 0:
            return "South" if self.walked else "East"
        else:
            return self.dirNames[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# @lc code=end