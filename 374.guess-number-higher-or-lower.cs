/*
 * @lc app=leetcode id=374 lang=csharp
 *
 * [374] Guess Number Higher or Lower
 */

// @lc code=start
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame 
{
    public int GuessNumber(int n) 
    {
        long l = 1;
        long r = n;
        long mid = 0;
        while (l <= r)
        {
            mid = (l + r) / 2;
            if (guess((int) mid) == -1)
            {
                r = mid - 1;
            }
            else if (guess((int) mid) == 1)
            {
                l = mid + 1;
            }
            else
            {
                return (int) mid;
            }
        }
        return (int) mid;   
    }
}
// @lc code=end

