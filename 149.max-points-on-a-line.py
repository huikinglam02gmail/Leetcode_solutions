#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
from typing import List


class Solution:
    # This problem is straightforward in concept: consider all different point pairs from left to right and store their gcd divided slopes as hash keys and add the points into the slope hash table
    # For all straight lines, they can be expressed as y = mx + b
    # y1x2 - y2x1 = b(x2-x1)
    # Slope are stored in terms of gcd divided numerator and denominator pairs: negatives are always in the numerator
    def gcd(self, a, b):
        if a < b:
            a,b = b,a
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort(key = lambda x: [x[0], x[1]])
        hash_table = {}
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                x_diff = x2 - x1

                if x_diff == 0:
                    if x1 not in hash_table:
                        hash_table[x1] = set()
                    hash_table[x1].add((x1,y1))
                    hash_table[x1].add((x2,y2))
                else:
                    y_diff = y2 - y1
                    intercept = y1*x2 - y2*x1                    
                    if y_diff < 0:
                        factor = self.gcd(x_diff, -y_diff)
                        key1 = (-(-y_diff // factor), x_diff // factor)
                    else:
                        factor = self.gcd(x_diff, y_diff)
                        key1 = (y_diff // factor, x_diff // factor)
                    if intercept < 0:
                        factor = self.gcd(x_diff, -intercept)
                        key2 = (-(-intercept // factor), x_diff // factor)
                    else:
                        factor = self.gcd(x_diff, intercept)
                        key2 = (intercept // factor, x_diff // factor)
                    key = (key1[0], key1[1], key2[0], key2[1])
                    if key not in hash_table:
                        hash_table[key] = set()
                    hash_table[key].add((x1, y1))
                    hash_table[key].add((x2, y2))
        result = 0
        for key in list(hash_table.keys()):
            result = max(result, len(list(hash_table[key])))
        return result
# @lc code=end

