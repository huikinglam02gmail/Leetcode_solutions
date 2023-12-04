/*
 * @lc app=leetcode id=2264 lang=csharp
 *
 * [2264] Largest 3-Same-Digit Number in String
 */

// @lc code=start
public class Solution {
    /**
     * Find "999" to "000" in num    
     */
    public string LargestGoodInteger(string num) {
        for (int i = 9; i >= 0; i--) {
            string search = new string((char)(i + '0'), 3);
            if (num.Contains(search)) return search;
        }
        return "";
    }
}

// @lc code=end

