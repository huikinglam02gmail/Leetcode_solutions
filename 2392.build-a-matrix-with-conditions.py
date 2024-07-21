#
# @lc app=leetcode id=2392 lang=python3
#
# [2392] Build a Matrix With Conditions
#

# @lc code=start
from typing import List


class Solution:
    '''
    # The conditions are asking for topological sort of the numbers, but in both rows and columns
    # I borrowed lee215's code of bfs-based topological sorting in 207. Course Schedule
    # It is a little different because in that problem the precedence of i and j is inverted and in this problem it used 1-indexed numbers
    # Another difference is we need to remove duplicates in here
    # I first assign 0 to len(topologically sorted sequence) to the sequence, and the rest of numbers are assigned according to the value
    # Repeat for row and columns    
    '''            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for i, j in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0: bfs.append(j)
        if len(bfs) == numCourses: self.sequence.append(bfs)
        return len(bfs) == numCourses
    
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        course_row, course_col = [], []
        row_seen, col_seen = set(), set()
        for i, j in rowConditions:
            if (i,j) not in row_seen: course_row.append([i-1, j-1])
            row_seen.add((i,j))
        for i, j in colConditions:
            if (i,j) not in col_seen: course_col.append([i-1, j-1])
            col_seen.add((i,j))
        self.sequence = []
        if not self.canFinish(k, course_row): return []
        if not self.canFinish(k, course_col): return []
        result = [[0 for i in range(k)] for j in range(k)]
        assignments = [[-1 for i in range(k)] for j in range(2)]
        for i in range(2):
            for j in range(len(self.sequence[i])):
                assignments[i][self.sequence[i][j]] = j

        for j in range(2):
            count = len(self.sequence[j])
            for i in range(k):
                if assignments[j][i] < 0:
                    assignments[j][i] = count
                    count += 1
        for i in range(k): result[assignments[0][i]][assignments[1][i]] = i + 1
        return result
# @lc code=end

