/*
 * @lc app=leetcode id=1558 lang=csharp
 *
 * [1558] Minimum Numbers of Function Calls to Make Target Array
 */

// @lc code=start
public class Solution 
{
    public int MinOperations(int[] nums) 
    {
        Dictionary<int, int> dict1 = new Dictionary<int, int>();
        Dictionary<int, int> dict2 = new Dictionary<int, int>();
        int result = 0;

        foreach(int num in nums)
        {
            if (!dict1.ContainsKey(num))
            {
                dict1[num] = 0;
            }
            dict1[num]++;
        }    

        while (dict1.Count > 0)
        {
            dict2.Clear();
            foreach (int key in dict1.Keys)
            {
                int key2 = key;
                if ((key2 & 1) > 0)
                {
                    result += dict1[key];
                    key2--;
                }
                key2 = key2 / 2;
                if (key2 > 0)
                {
                    if (!dict2.ContainsKey(key2))
                    {
                        dict2[key2] = 0;
                    }
                    dict2[key2] += dict1[key];
                }
            }
            if (dict2.Count > 0)
            {
                result++;
            }
            dict1 = dict2.ToDictionary(entry => entry.Key, entry => entry.Value);
        }
        return result;
    }
}
// @lc code=end

