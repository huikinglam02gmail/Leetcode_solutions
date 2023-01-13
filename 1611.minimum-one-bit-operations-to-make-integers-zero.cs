/*
 * @lc app=leetcode id=1611 lang=csharp
 *
 * [1611] Minimum One Bit Operations to Make Integers Zero
 */

// @lc code=start
public class Solution 
{
    public int Size(int bits)
    {
        int size = 0;
        while(bits != 0)
        {
            bits >>= 1;
            size++;
        }
        return size;
    }
    public int MinimumOneBitOperations(int n) 
    {
        if (n == 0)
        {
            return 0;
        }
        int l = Size(n);
        return (1 << l) - 1 - MinimumOneBitOperations(n - (1 << (l - 1)));
    }
}
// @lc code=end

