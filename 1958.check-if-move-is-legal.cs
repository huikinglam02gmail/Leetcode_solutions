/*
 * @lc app=leetcode id=1958 lang=csharp
 *
 * [1958] Check if Move is Legal
 */

// @lc code=start
public class Solution {
    public bool CheckMove(char[][] board, int rMove, int cMove, char color) {
        int m = board.Length;
        int n = board[0].Length;
        
        int[][] steps = new int[][] {
            new int[] { 1, 0 },
            new int[] { 1, 1 },
            new int[] { 0, 1 },
            new int[] { -1, 1 },
            new int[] { -1, 0 },
            new int[] { -1, -1 },
            new int[] { 0, -1 },
            new int[] { 1, -1 }
        };

        Dictionary<char, char> opp = new Dictionary<char, char>() {
            { 'B', 'W' },
            { 'W', 'B' }
        };

        for (int i = 0; i < 8; i++) {
            int x = rMove;
            int y = cMove;
            int countDiff = 0;
            
            while (x + steps[i][0] >= 0 && x + steps[i][0] < m && y + steps[i][1] >= 0 && y + steps[i][1] < n) {
                x += steps[i][0];
                y += steps[i][1];
                
                if (board[x][y] == opp[color]) {
                    countDiff++;
                }
                else if (board[x][y] == color && countDiff > 0) {
                    return true;
                }
                else {
                    break;
                }
            }
        }
        
        return false;
    }
}

// @lc code=end

