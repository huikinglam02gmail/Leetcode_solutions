/*
 * @lc app=leetcode id=1442 lang=csharp
 *
 * [1442] Count Triplets That Can Form Two Arrays of Equal XOR
 */

// @lc code=start
public class Solution
{
    public int CountTriplets(int[] arr)
    {
        List<int> prefix = new List<int>();
        Dictionary<int, List<int>> Seen = new Dictionary<int, List<int>>();
        int n = arr.Length;
        int result = 0;

        prefix.Add(0);
        Seen.Add(0,new List<int> {0});
        for (int i = 0; i < n; i++)
        {
            prefix.Add(prefix[prefix.Count()-1]^arr[i]);
            if (Seen.ContainsKey(prefix[prefix.Count()-1]))
            {
                foreach (int j in Seen[prefix[prefix.Count()-1]])
                {
                    result += i - j;
                }
            }
            else
            {
                Seen.Add(prefix[prefix.Count()-1], new List<int>());
            }
            Seen[prefix[prefix.Count()-1]].Add(i + 1);
        }
        return result;    
    }
}
// @lc code=end

