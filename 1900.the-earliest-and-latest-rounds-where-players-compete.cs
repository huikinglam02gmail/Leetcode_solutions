/*
 * @lc app=leetcode id=1900 lang=csharp
 *
 * [1900] The Earliest and Latest Rounds Where Players Compete
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private int n;
    private int firstPlayer;
    private int secondPlayer;
    private Dictionary<Tuple<int, int, int>, int[]> memo;

    public int[] EarliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        this.n = n;
        this.firstPlayer = firstPlayer;
        this.secondPlayer = secondPlayer;
        this.memo = new Dictionary<Tuple<int, int, int>, int[]>();

        return DP((1 << n) - 1, 0, 1);
    }

    private int[] DP(int competitors, int winners, int round) {
        Tuple<int, int, int> t = new Tuple<int, int, int>(competitors, winners, round);
        if (!memo.ContainsKey(t)) 
        {
            int[] result = new int[2] { int.MaxValue, 0 };

            if (competitors == 0)
            {
                result = DP(winners, 0, round + 1);
            }
            else
            {
                int l = 0, r = n - 1;

                while (l < n && (competitors & (1 << l)) == 0)
                {
                    l++;
                }

                while (r >= 0 && (competitors & (1 << r)) == 0)
                {
                    r--;
                }

                competitors ^= (1 << l);

                if (l < r)
                {
                    competitors ^= (1 << r);
                }

                if (l == firstPlayer - 1 && r == secondPlayer - 1)
                {
                    result = new int[2] { round, round };
                }
                else if (l == firstPlayer - 1 || l == secondPlayer - 1)
                {
                    result = DP(competitors, winners ^ (1 << l), round);
                }
                else if (r == firstPlayer - 1 || r == secondPlayer - 1)
                {
                    result = DP(competitors, winners ^ (1 << r), round);
                }
                else
                {
                    int[] leftWins = DP(competitors, winners ^ (1 << l), round);
                    int[] rightWins = DP(competitors, winners ^ (1 << r), round);
                    result[0] = Math.Min(leftWins[0], rightWins[0]);
                    result[1] = Math.Max(leftWins[1], rightWins[1]);
                }
            }
            memo[t] = result;
        }
        return memo[t];
    }
}

// @lc code=end

