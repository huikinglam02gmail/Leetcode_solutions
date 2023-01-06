/*
 * @lc app=leetcode id=1590 lang=csharp
 *
 * [1590] Make Sum Divisible by P
 */

// @lc code=start
public class Solution 
{
    public int MinSubarray(int[] nums, int p) 
    {
        long total = nums.Sum(x => (long) x);
        if (total % p == 0)
        {
            return 0;
        }
        else if (total < p)
        {
            return -1;
        }
        else
        {
            List<long> prefix = new List<long>() {0};
            Dictionary<long, int> hashTable = new Dictionary<long, int>();
            hashTable.Add(0, -1);
            int n = nums.Length;
            int result = n;

            for (int i = 0; i < n; i++)
            {
                prefix.Add(prefix[prefix.Count - 1] + nums[i]);
                long keyToLookFor = (p + prefix[prefix.Count - 1] % p - total % p) % p;
                if (hashTable.ContainsKey(keyToLookFor))
                {
                   result = Math.Min(result, i - hashTable[keyToLookFor]);
                }
                
                hashTable[prefix[prefix.Count - 1] % p] = i;
            }
            if (result < n)
            {
                return result;
            }
            else
            {
                return -1;
            }
        }    
    }
}
// @lc code=end
