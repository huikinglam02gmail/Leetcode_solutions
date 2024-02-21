/*
 * @lc app=leetcode id=201 lang=csharp
 *
 * [201] Bitwise AND of Numbers Range
 */

// @lc code=start
public class Solution {
    public int RangeBitwiseAnd(int left, int right) {
        if (left == right) return left;
        else {
            int leftCount = 0;
            int temp = left;
            while (temp > 0) {
                leftCount++;
                temp /= 2;
            }
            int rightCount = 0;
            temp = right;
            while (temp > 0) {
                rightCount++;
                temp /= 2;
            }
            if (leftCount != rightCount) {
                return 0;
            } else {
                left -= 1 << (leftCount - 1);
                right -= 1 << (rightCount - 1);
                return (1 << (leftCount - 1)) + RangeBitwiseAnd(left, right);
            }
        }
    }
}

// @lc code=end

