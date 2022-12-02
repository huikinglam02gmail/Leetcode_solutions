/*
 * @lc app=leetcode id=1207 lang=csharp
 *
 * [1207] Unique Number of Occurrences
 */

// @lc code=start
public class Solution 
{
    public bool UniqueOccurrences(int[] arr) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        HashSet<int> freq = new HashSet<int>();
        foreach (int num in arr)
        {
            if (!hashTable.ContainsKey(num))
            {
                hashTable[num] = 0;
            }
            hashTable[num] += 1;
        }
        foreach (int value in hashTable.Values)
        {
            if (!freq.Contains(value))
            {
                freq.Add(value);
            }
            else
            {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

