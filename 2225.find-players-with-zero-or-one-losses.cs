/*
 * @lc app=leetcode id=2225 lang=csharp
 *
 * [2225] Find Players With Zero or One Losses
 */

// @lc code=start
public class Solution 
{
    public IList<IList<int>> FindWinners(int[][] matches) 
    {
        SortedDictionary<int, int[]> hashTable = new SortedDictionary<int, int[]>();
        List<IList<int>> result = new List<IList<int>>();
        result.Add(new List<int>());
        result.Add(new List<int>());
        foreach (int[] players in matches)
        {
            if (!hashTable.ContainsKey(players[0]))
            {
                hashTable.Add(players[0], new int[2] {0, 0});
            }
            if (!hashTable.ContainsKey(players[1]))
            {
                hashTable.Add(players[1], new int[2] {0, 0});
            }
            hashTable[players[0]][0]++;
            hashTable[players[1]][1]++;
        }
        foreach (int key in hashTable.Keys)
        {
            if (hashTable[key][1] == 0)
            {
                result[0].Add(key);
            }
            else if (hashTable[key][1] == 1)
            {
                result[1].Add(key);
            }
        }
        return result;
    }
}
// @lc code=end

