/*
 * @lc app=leetcode id=1630 lang=csharp
 *
 * [1630] Arithmetic Subarrays
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

    public IList<bool> CheckArithmeticSubarrays(int[] nums, int[] l, int[] r) 
    {
        List<bool> result = new List<bool>();
        for (int i = 0; i < l.Length; i++)
        {
            result.Add(CanMakeArithmeticProgression());
        }
        return result;   
    }
}
// @lc code=end

