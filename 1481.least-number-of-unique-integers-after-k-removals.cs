/*
 * @lc app=leetcode id=1481 lang=csharp
 *
 * [1481] Least Number of Unique Integers after K Removals
 */

// @lc code=start
public class Solution 
{
    public int FindLeastNumOfUniqueInts(int[] arr, int k) 
    {
        Dictionary<int, int> occur = new Dictionary<int, int>();
        foreach (int num in arr) 
        {
            if (!occur.ContainsKey(num))
            {
                occur.Add(num, 0);
            }
            occur[num]++;
        }

        List<int> values = occur.Values.ToList();
        values.Sort();
        int n = values.Count();
        int i = 0;
        while (k > 0)
        {
            if (values[i] <= k)
            {
                k -= values[i];
                i += 1;
            }
            else
            {
                k = 0;
            }
        }
        return n - i;
    }
}
// @lc code=end

