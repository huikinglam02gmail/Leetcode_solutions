/*
 * @lc app=leetcode id=1702 lang=csharp
 *
 * [1702] Maximum Binary String After Change
 */

// @lc code=start
public class Solution 
{
    public string MaximumBinaryString(string binary) 
    {
        int i = 0;
        int j = 0; 
        int p = 0;    
        int n = binary.Length;
        while (i < n && binary[i] == '1')
        {
            p++;
            i++;
        }
        while (i < n)
        {
            if (binary[i] == '0')
            {
                j++;
            }
            i++;
        }
        return n == p ? binary : string.Concat(string.Concat(Enumerable.Repeat('1', p + j - 1)),"0", string.Concat(Enumerable.Repeat('1', n - p - j)));
    }
}
// @lc code=end

