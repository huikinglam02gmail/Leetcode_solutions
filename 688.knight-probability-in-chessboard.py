#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
class Solution:
    '''
    Given n and current position we can calculate the probability for the knight to be at i,j on board for the next round
    Also we do not need to consider fraction. just sum up and divide by pow(8,k)        
    '''   
    def inside_board(self, row, col, n):
        return 0 <= row < n and 0 <= col < n
    
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        possible_steps =  [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
        destination = [[[] for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                for l in range(8):
                    if self.inside_board(i + possible_steps[l][0], j + possible_steps[l][1], n):
                        destination[i][j].append([i + possible_steps[l][0], j + possible_steps[l][1]])

        dp_old = [[0 for i in range(n)] for j in range(n)]
        dp_old[row][column] = 1
        
        for run in range(k):
            dp_new = [[0 for i in range(n)] for j in range(n)]
            for i in range(n):
                for j in range(n):
                    if dp_old[i][j] > 0:
                        for item in destination[i][j]:
                            dp_new[item[0]][item[1]] += dp_old[i][j]
            dp_old = dp_new
        
        result = 0
        for i in range(n):
            for j in range(n):
                result += dp_old[i][j]
        return result / pow(8, k)
# @lc code=end

