#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0 for j in range(n)] for i in range(m)]
        for i in range(len(img)):
            for j in range(len(img[0])):
                avg = 0
                counter = 0
                for k in range(-1,2,1):
                    for l in range(-1,2,1):
                        if 0 <= i + k < len(img) and 0 <= j + l < len(img[0]):
                            avg += img[i+k][j+l]
                            counter += 1
                result[i][j] = avg // counter
        return result
# @lc code=end

