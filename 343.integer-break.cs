/*
 * @lc app=leetcode id=343 lang=csharp
 *
 * [343] Integer Break
 */

// @lc code=start
public class Solution {
    /*
    If an optimal product contains a factor f >= 4, then you can replace it with factors 2 and f-2 without losing optimality, as 2*(f-2) = 2f-4 >= f.
    So you never need a factor greater than or equal to 4, meaning you only need factors 1, 2 and 3 (and 1 is of course wasteful and you'd only use it for n=2 and n=3, where it's needed).
    */
    public int IntegerBreak(int n) {
        if (n == 2) {
            return 1;
        }
        else if (n == 3) {
            return 2;
        }
        else {
            int result = 1;
            while (n > 4) {
                n -= 3;
                result *= 3;
            }
            return n * result;
        }
    }
}

// @lc code=end

