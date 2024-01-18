/*
 * @lc app=leetcode id=2525 lang=csharp
 *
 * [2525] Categorize Box According to Criteria
 */

// @lc code=start
public class Solution {
    /**
     * Set bulky and heavy as booleans
     */
    public string CategorizeBox(int length, int width, int height, int mass) {
        bool bulky = length >= 10000 || width >= 10000 || height >= 10000 || (long)length * (long)width * (long)height >= (long)1000000000;
        bool heavy = mass >= 100;
        
        if (bulky && heavy) {
            return "Both";
        } else if (bulky) {
            return "Bulky";
        } else if (heavy) {
            return "Heavy";
        } else {
            return "Neither";
        }
    }
}

// @lc code=end

