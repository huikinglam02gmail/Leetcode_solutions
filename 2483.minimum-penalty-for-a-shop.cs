/*
 * @lc app=leetcode id=2483 lang=csharp
 *
 * [2483] Minimum Penalty for a Shop
 */

// @lc code=start
public class Solution {
    public int BestClosingTime(string customers) {
        int n = customers.Length;
        int result = n;
        int minimum = -customers.Count(c => c == 'N');
        int current = minimum;
        
        for (int i = n - 1; i >= 0; i--) {
            if (customers[i] == 'N') {
                current -= 1;
            }
            else {
                current += 1;
            }
            if (current <= minimum) {
                minimum = current;
                result = i;
            }
        }
        
        return result;
    }
}

// @lc code=end

