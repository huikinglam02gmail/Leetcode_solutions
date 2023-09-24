#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    '''
    The only plausible way to go is to simulate    
    Because query_row limit is only 100, one can just stop the filling process and return 0    
    '''
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for i in range(query_row + 1):
            nxt = [0]*(len(row) + 1)
            for j in range(len(row)):
                if row[j] < 1:
                    if i == query_row and j == query_glass:
                        return row[j]
                else:
                    nxt[j] += (row[j] - 1) / 2
                    nxt[j + 1] += (row[j] - 1) / 2
                    row[j] = 1
            row = nxt[:]
        return 1
# @lc code=end

