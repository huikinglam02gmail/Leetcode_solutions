/*
 * @lc app=leetcode id=1888 lang=csharp
 *
 * [1888] Minimum Number of Flips to Make the Binary String Alternating
 */

// @lc code=start
public class Solution {
    public int MinFlips(string s) {
        int[,] parity = new int[2, 2];
        int n = s.Length;
        int result = n;

        for (int i = 0; i < n; i++) {
            parity[i % 2, s[i] - '0']++;
        }

        for (int i = 0; i < n; i++) {
            result = Math.Min(result, parity[1, 0] + parity[0, 1]);
            result = Math.Min(result, parity[0, 0] + parity[1, 1]);
            parity[0, s[i] - '0']--;
            int temp = parity[0, 0];
            parity[0, 0] = parity[1, 0];
            parity[1, 0] = temp;
            temp = parity[0, 1];
            parity[0, 1] = parity[1, 1];
            parity[1, 1] = temp;
            parity[(n - 1) % 2, s[i] - '0']++;
        }

        return result;
    }
}

// @lc code=end

