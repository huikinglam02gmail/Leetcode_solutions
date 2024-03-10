/*
 * @lc app=leetcode id=3014 lang=csharp
 *
 * [3014] Minimum Number of Pushes to Type Word I
 */

// @lc code=start
public class Solution {
    public int MinimumPushes(string word) {
        int result = 0;
        int n = word.Length;
        for (int i = 0; i < n; i++) {
            result += 1 + (i / 8);
        }
        return result;
    }
}

// @lc code=end

