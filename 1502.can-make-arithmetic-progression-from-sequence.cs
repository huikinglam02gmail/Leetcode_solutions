/*
 * @lc app=leetcode id=1502 lang=csharp
 *
 * [1502] Can Make Arithmetic Progression From Sequence
 */

// @lc code=start
public class Solution 
{
    public bool CanMakeArithmeticProgression(int[] arr) 
    {
        Array.Sort(arr);
        int diff = arr[1] - arr[0];
        int n = arr.Length;
        for (int i = 1; i < n - 1; i++)
        {
            if (arr[i] + diff != arr[i + 1])
            {
                return false;
            }
        }     
        return true;
    }
}
// @lc code=end

