#
# @lc app=leetcode id=1970 lang=python3
#
# [1970] Last Day Where You Can Still Cross
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    4 <= row * col <= 2 * 10^4
    cells.length == row * col = n
    As the answer must be smaller than or equal to 2 * 10^4, so we binary search for the answer O(log n). For each test answer, build the graph O(n) and BFS from top O(col) ~ O(n).  
    '''
    def canPass(self):
        visited = set()
        for j in range(self.col):
            if (0, j) not in visited and (0, j) not in self.sea:
                dq = deque()
                dq.append((0, j))
                visited.add((0, j))
                while dq:
                    x, y = dq.popleft()
                    if x == self.row - 1:
                        return True
                    neigs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                    for neig in neigs:
                        if neig not in visited and neig not in self.sea and 0 <= neig[0] < self.row and 0 <= neig[1] < self.col:
                            visited.add(neig)
                            dq.append(neig)
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.sea = set()
        self.row = row
        self.col = col
        l, r = 0, row * col
        while l < r:
            mid = l + (r - l) // 2
            self.sea = set([tuple([cell[0] - 1, cell[1] - 1]) for cell in cells[: mid]])
            if self.canPass():
                l = mid + 1
            else:
                r = mid
        return l - 1
        
        
# @lc code=end

