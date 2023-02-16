/*
 * @lc app=leetcode id=989 lang=csharp
 *
 * [989] Add to Array-Form of Integer
 */

// @lc code=start
public class Solution 
{
    public IList<int> AddToArrayForm(int[] num, int k) 
    {
        int passOver = 0;
        int n =  num.Length;
        List<int> result = new List<int>();
        for (int i = n - 1; i >= 0; i --)
        {
            k = Math.DivRem(k, 10, out int d);
            passOver = Math.DivRem(num[i] + d + passOver, 10, out int N);
            result.Add(N);
        }
        while (k > 0)
        {
            k = Math.DivRem(k, 10, out int d);
            passOver = Math.DivRem(d + passOver, 10, out int N);
            result.Add(N);
        }
        if (passOver > 0)
        {
            result.Add(1);
        }
        result.Reverse();
        return result;
    }
}
// @lc code=end

