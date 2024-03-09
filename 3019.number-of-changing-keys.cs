/*
 * @lc app=leetcode id=3019 lang=csharp
 *
 * [3019] Number of Changing Keys
 */

// @lc code=start
public class Solution {
    public int CountKeyChanges(string s) {
        int result = 0;
        int n = s.Length;
        for (int i = 0; i < n - 1; i++) {
            if (char.ToLower(s[i + 1]) != char.ToLower(s[i])) result++;
        }
        return result;
    }
}

// @lc code=end

