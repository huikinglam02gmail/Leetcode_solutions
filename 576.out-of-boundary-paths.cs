/*
 * @lc app=leetcode id=576 lang=csharp
 *
 * [576] Out of Boundary Paths
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /**
     * DP problem
     * Count the number of times the ball can arrive at the edge for each number of moves
     */
    private int Scores(int row, int col, int m, int n)
    {
        int count = 0;
        if (row == 0)
        {
            count += 1;
        }
        if (col == 0)
        {
            count += 1;
        }
        if (row == m - 1)
        {
            count += 1;
        }
        if (col == n - 1)
        {
            count += 1;
        }
        return count;
    }

    public int FindPaths(int m, int n, int maxMove, int startRow, int startColumn)
    {
        long[][] dp = new long[m][];
        for (int i = 0; i < m; i++)
        {
            dp[i] = new long[n];
        }

        long MOD = 1000000007;
        // Get the coordinates of hash map of corners and edges to store the number of exit ways
        Dictionary<(int, int), long> hashTable = new Dictionary<(int, int), long>();
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int score = Scores(i, j, m, n);
                if (score > 0)
                {
                    hashTable[(i, j)] = score;
                }
            }
        }

        long result = 0;
        // Keep counting numbers of balls possible in each position
        // Count the edge and corners scores * the dp count
        for (int move = 0; move < maxMove; move++)
        {
            if (move == 0)
            {
                dp[startRow][startColumn] = 1;
                if (hashTable.ContainsKey((startRow, startColumn)))
                {
                    result += hashTable[(startRow, startColumn)];
                    result %= MOD;
                }
            }
            else
            {
                long[][] dpNew = new long[m][];
                for (int i = 0; i < m; i++)
                {
                    dpNew[i] = new long[n];
                }

                for (int i = 0; i < m; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        if (i >= 1)
                        {
                            dpNew[i][j] += dp[i - 1][j];
                            dpNew[i][j] %= MOD;
                        }
                        if (j >= 1)
                        {
                            dpNew[i][j] += dp[i][j - 1];
                            dpNew[i][j] %= MOD;
                        }
                        if (i < m - 1)
                        {
                            dpNew[i][j] += dp[i + 1][j];
                            dpNew[i][j] %= MOD;
                        }
                        if (j < n - 1)
                        {
                            dpNew[i][j] += dp[i][j + 1];
                            dpNew[i][j] %= MOD;
                        }
                        if (hashTable.ContainsKey((i, j)))
                        {
                            result += dpNew[i][j] * hashTable[(i, j)];
                            result %= MOD;
                        }
                    }
                }
                dp = dpNew;
            }
        }

        return Convert.ToInt32(result);
    }
}

// @lc code=end

