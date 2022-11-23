/*
 * @lc app=leetcode id=1486 lang=csharp
 *
 * [1486] XOR Operation in an Array
 */

// @lc code=start
public class Solution 
{
    public int prefix(int endNum)
    {
        int n = 0;
        if (endNum % 2 == 0)
        {
            n = endNum / 2;
        }
        else
        {
            n = (endNum - 1) / 2;
        }
        if (n % 4 == 0)
        {
            return endNum;
        }
        else if (n % 4 == 2)
        {
            return endNum ^ 2;
        }
        else if (n % 4 == 1)
        {
            return 2;
        }
        else
        {
            return 0;
        }
    }
    public int XorOperation(int n, int start) 
    {
        int end = start + 2*(n-1);
        if (start > 1)
        {
            return prefix(end) ^ prefix(start-2);
        }
        else
        {
            return prefix(end);
        }
    }
}
// @lc code=end

