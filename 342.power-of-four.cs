/*
 * @lc app=leetcode id=342 lang=csharp
 *
 * [342] Power of Four
 */

// @lc code=start
public class Solution {
    public bool IsPowerOfFour(int n) 
    {
        if (n > 0) 
        {
            string nBinary = Convert.ToString(n, 2);
            char[] nBinaryArray = nBinary.ToCharArray();
            Array.Reverse(nBinaryArray);
            nBinary = new string(nBinaryArray);

            if (nBinary.Count(c => c == '1') == 1 && nBinary.IndexOf('1') % 2 == 0) {
                return true;
            }
        }
        return false;
    }
}

// @lc code=end

