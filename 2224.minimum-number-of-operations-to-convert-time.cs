/*
 * @lc app=leetcode id=2224 lang=csharp
 *
 * [2224] Minimum Number of Operations to Convert Time
 */

// @lc code=start
public class Solution {
    public int ConvertTime(string current, string correct) {
        int correctTime = int.Parse(correct.Substring(0, 2)) * 60 + int.Parse(correct.Substring(3));
        int currentTime = int.Parse(current.Substring(0, 2)) * 60 + int.Parse(current.Substring(3));
        int result = 0;

        foreach (int increment in new int[] { 60, 15, 5, 1 }) {
            int inc = (correctTime - currentTime) / increment;
            currentTime += inc * increment;
            result += inc;
        }

        return result;
    }
}

// @lc code=end

