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
        Dictionary<int, Dictionary<int,int>> hashTableEnd = new Dictionary<int, Dictionary<int,int>>();
        int n = arr.Length;
        int result = 0;

        prefix.Add(0);
        for (int i = 0; i < n; i++)
        {
            prefix.Add(prefix[prefix.Count()-1]^arr[i]);
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = i+1; j < n+1; j++)
            {
                int pair = prefix[i]^prefix[j];
                if (!hashTableEnd.ContainsKey(pair))
                {
                    hashTableEnd[pair] = new Dictionary<int, int>();
                }
                if (!hashTableEnd[pair].ContainsKey(j))
                {
                    hashTableEnd[pair][j] = 0;
                }
                hashTableEnd[pair][j] += 1;
                if  (hashTableEnd[pair].ContainsKey(i))
                {
                    result += hashTableEnd[pair][i];
                }                
            }
        }
        return result;    
    }
}
// @lc code=end

