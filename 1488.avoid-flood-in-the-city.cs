/*
 * @lc app=leetcode id=1488 lang=csharp
 *
 * [1488] Avoid Flood in The City
 */

// @lc code=start
public class Solution 
{
    public int[] AvoidFlood(int[] rains) 
    {
        Dictionary<int, List<int>> Record = new Dictionary<int, List<int>>();
        PriorityQueue<int, int> coming = new PriorityQueue<int, int>();
        HashSet<int> full = new HashSet<int>();
        int[] result = new int[rains.Length];
        for (int i = 0; i < rains.Length; i++)
        {
            if (!Record.ContainsKey(rains[i]))
            {
                Record.Add(rains[i], new List<int>());
            }
            Record[rains[i]].Add(i);
        }
        for (int i = 0; i < rains.Length; i++)
        {
            if (rains[i] > 0)
            {
                if (full.Contains(rains[i]))
                {
                    return new int[] {};
                }
                else
                {
                    full.Add(rains[i]);
                    int ind = Record[rains[i]].BinarySearch(i);
                    if (ind + 1 < Record[rains[i]].Count)
                    {
                        coming.Enqueue(rains[i], Record[rains[i]][ind + 1]);
                    }
                    result[i] = -1;
                }
            }
            else
            {
                if (coming.Count > 0)
                {
                    int lake = coming.Dequeue();
                    full.Remove(lake);
                    result[i] = lake;
                }
                else
                {
                    result[i] = 1;
                }
            }
        }
        return result;
    }
}
// @lc code=end

