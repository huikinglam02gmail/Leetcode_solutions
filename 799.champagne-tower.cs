/*
 * @lc app=leetcode id=799 lang=csharp
 *
 * [799] Champagne Tower
 */

// @lc code=start
public class Solution {
    public double ChampagneTower(int poured, int query_row, int query_glass) {
        double[] row = new double[query_row + 1];
        row[0] = poured;

        for (int i = 0; i <= query_row; i++) {
            double[] next = new double[row.Length + 1];

            for (int j = 0; j < row.Length; j++) {
                if (row[j] < 1) {
                    if (i == query_row && j == query_glass) {
                        return row[j];
                    }
                } else {
                    next[j] += (row[j] - 1) / 2;
                    next[j + 1] += (row[j] - 1) / 2;
                    row[j] = 1;
                }
            }

            row = next;
        }

        return 1;
    }
}

// @lc code=end

