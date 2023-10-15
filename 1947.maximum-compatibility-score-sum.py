#
# @lc app=leetcode id=1947 lang=python3
#
# [1947] Maximum Compatibility Score Sum
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    Backtracking
    Use bitmasks to represent student and mentor
    '''
    @lru_cache(None)
    def compatibilityScore(self, i, j):
        return sum([1- (self.students[i][k] ^ self.mentors[j][k]) for k in range(self.n)])

    @lru_cache(None)
    def backtracking(self, studentMask, mentorMask):
        result = 0
        for i in range(self.m):
            for j in range(self.m):
                if studentMask & (1 << i) == 0 and mentorMask & (1 << j) == 0:
                    result = max(result, self.compatibilityScore(i, j) + self.backtracking(studentMask ^ (1 << i), mentorMask ^ (1 << j)))
        return result

    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        self.students = students
        self.mentors = mentors
        self.m = len(students)
        self.n = len(students[0])
        return self.backtracking(0, 0)
# @lc code=end

