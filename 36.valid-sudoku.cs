/*
 * @lc app=leetcode id=36 lang=csharp
 *
 * [36] Valid Sudoku
 */

// @lc code=start
public class Solution 
{
    public bool IsValidSudoku(char[][] board) 
    {
        HashSet<char> seen = new HashSet<char>();
        for (int i = 0; i < 9; i++)
        {
            seen.Clear();
            for (int j = 0; j < 9; j++)
            {
                if (board[i][j] != '.')
                {
                    if (seen.Contains(board[i][j]))
                    {
                        return false;
                    }
                    else
                    {
                        seen.Add(board[i][j]);
                    }
                }
            }
        }
        for (int i = 0; i < 9; i++)
        {
            seen.Clear();
            for (int j = 0; j < 9; j++)
            {
                if (board[j][i] != '.')
                {
                    if (seen.Contains(board[j][i]))
                    {
                        return false;
                    }
                    else
                    {
                        seen.Add(board[j][i]);
                    }
                }
            }
        }
        for (int k = 0; k < 9; k = k+3)
        {
            for (int l = 0; l < 9; l = l+3)
            {
                seen.Clear();
                for (int i = k; i < k+3; i++)
                {
                    for (int j = l; j < l+3; j++)
                    {
                        if (board[i][j] != '.')
                        {
                            if (seen.Contains(board[i][j]))
                            {
                                return false;
                            }
                            else
                            {
                                seen.Add(board[i][j]);
                            }
                        }
                    }
                } 
            }
        }
        return true;
    }
}
// @lc code=end

