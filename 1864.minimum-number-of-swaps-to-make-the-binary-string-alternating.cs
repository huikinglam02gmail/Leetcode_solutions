/*
 * @lc app=leetcode id=1864 lang=csharp
 *
 * [1864] Minimum Number of Swaps to Make the Binary String Alternating
 */

// @lc code=start
public class Solution {
    public int MinSwaps(string s) {
        int count0 = 0;
        foreach (char c in s) {
            if (c == '0') {
                count0++;
            }
        }
        int n = s.Length;
        if (Math.Abs(2 * count0 - n) > (n % 2)) {
            return -1;
        }
        else {
            int[] zeroInWrongPlace = new int[2];
            if (count0 == n - count0 - 1) {
                zeroInWrongPlace[0] = n;
            }
            if (count0 == n - count0 + 1) {
                zeroInWrongPlace[1] = n;
            }
            for (int i = 0; i < n; i++) {
                if (s[i] == '0') {
                    if (i % 2 == 0) {
                        zeroInWrongPlace[1]++;
                    }
                    else {
                        zeroInWrongPlace[0]++;
                    }
                }
            }
            return Math.Min(zeroInWrongPlace[0], zeroInWrongPlace[1]);
        }
    }
}

// @lc code=end

