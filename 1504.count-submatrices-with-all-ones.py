#
# @lc app=leetcode id=1504 lang=python3
#
# [1504] Count Submatrices With All Ones
#

# @lc code=start
class Solution:
    # Same problem as maximum rectangle in histogram
    # can be solved by monotonic stack row by row
    # for each row, find out the height of columns going up from the mat[i][j]
    # By organizing a monotonic decreasing stack, we count the number of full 1 rectangles with [i,j] being the bottom right corner
    # Need to be careful if current column is taller than previous column
    
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        last = [0]*n
        result = 0
        for i in range(m):
            stack = []
            BR = [0]*n
            for j in range(n):
                if mat[i][j] == 1:
                    last[j] += 1
                else:
                    last[j] = 0
                while stack and last[j] <= last[stack[-1]]:
                    stack.pop()
                if not stack:
                    BR[j] += last[j]*(j + 1)
                else:
                    BR[j] += last[j]*(j - stack[-1])
                    BR[j] += BR[stack[-1]]
                stack.append(j)
            result += sum(BR)                
        return result
# @lc code=end

