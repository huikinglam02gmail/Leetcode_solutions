/*
 * @lc app=leetcode id=2729 lang=csharp
 *
 * [2729] Check if The Number is Fascinating
 */

// @lc code=start
public class Solution {
    public bool IsFascinating(int n) {
        string resultString = "";
        for (int i = 1; i <= 3; i++) {
            resultString += (i * n).ToString();
        }
        for (int i = 1; i <= 9; i++) {
            if (resultString.Count(c => c == i.ToString()[0]) != 1) {
                return false;
            }
        }
        return true;
    }
}

// @lc code=end

