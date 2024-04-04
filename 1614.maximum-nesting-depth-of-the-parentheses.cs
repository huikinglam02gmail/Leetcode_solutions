/*
 * @lc app=leetcode id=1614 lang=csharp
 *
 * [1614] Maximum Nesting Depth of the Parentheses
 */

// @lc code=start
public class Solution {
    /*
    Keep track of which level you're at, and the historical max
    */
    public int MaxDepth(string s) {
        int currentMax = 0;
        int current = 0;
        foreach (char c in s) {
            if (c == '(') {
                current++;
                currentMax = Math.Max(currentMax, current);
            } else if (c == ')') {
                current--;
            }
        }
        return currentMax;
    }
}

// @lc code=end

