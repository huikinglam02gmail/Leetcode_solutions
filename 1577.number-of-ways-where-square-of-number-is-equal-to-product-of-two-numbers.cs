/*
 * @lc app=leetcode id=1577 lang=csharp
 *
 * [1577] Number of Ways Where Square of Number Is Equal to Product of Two Numbers
 */

// @lc code=start
public class Solution 
{
    public int NumTriplets(int[] nums1, int[] nums2) 
    {
        Dictionary<long, int> hashTable1 = new Dictionary<long, int>();
        Dictionary<long, int> hashTable2 = new Dictionary<long, int>(); 
        foreach (int num in nums1)
        {
            if (!hashTable1.ContainsKey(Convert.ToInt64(num)))
            {
                hashTable1[Convert.ToInt64(num)] = 0;
            }
            hashTable1[Convert.ToInt64(num)]++;
        }
        foreach (int num in nums2)
        {
            if (!hashTable2.ContainsKey(Convert.ToInt64(num)))
            {
                hashTable2[Convert.ToInt64(num)] = 0;
            }
            hashTable2[Convert.ToInt64(num)]++;
        }
        long result = 0;
        foreach (KeyValuePair<long, int> kvp1 in hashTable1)
        {
            foreach(KeyValuePair<long, int> kvp2 in hashTable2)
            {
                if ((kvp1.Key * kvp1.Key) % kvp2.Key == 0 && hashTable2.ContainsKey((kvp1.Key * kvp1.Key) / kvp2.Key))
                {
                    if (kvp1.Key == kvp2.Key)
                    {
                        result += kvp1.Value * kvp2.Value * (kvp2.Value - 1);
                    }
                    else
                    {
                        result += kvp1.Value * kvp2.Value * hashTable2[(kvp1.Key * kvp1.Key) / kvp2.Key];
                    }
                } 
            }
        }
        foreach (KeyValuePair<long, int> kvp2 in hashTable2)
        {
            foreach(KeyValuePair<long, int> kvp1 in hashTable1)
            {
                if ((kvp2.Key * kvp2.Key) % kvp1.Key == 0 && hashTable1.ContainsKey((kvp2.Key * kvp2.Key) / kvp1.Key))
                {
                    if (kvp2.Key == kvp1.Key)
                    {
                        result += kvp2.Value * kvp1.Value * (kvp1.Value - 1);
                    }
                    else
                    {
                        result += kvp2.Value * kvp1.Value * hashTable1[(kvp2.Key * kvp2.Key) / kvp1.Key];
                    }
                } 
            }
        }
        return Convert.ToInt32(result / 2);
    }
}
// @lc code=end

