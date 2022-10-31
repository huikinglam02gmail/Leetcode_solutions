/*
 * @lc app=leetcode id=1424 lang=csharp
 *
 * [1424] Diagonal Traverse II
 */

// @lc code=start
public class Solution {
    public int[] FindDiagonalOrder(IList<IList<int>> nums) {
        int m = nums.Count;
        int elementCount = 0;
        SortedDictionary<int, List<Tuple<int, int>>> hashTable = new SortedDictionary<int, List<Tuple<int, int>>>();
        for (int i = 0; i< m; i++)
        {
            int l = nums[i].Count;
            for (int j = 0; j < l; j++)
            {
                if (!hashTable.ContainsKey(i+j))
                {
                    hashTable.Add(i+j, new List<Tuple<int, int>>());
                }
                hashTable[i+j].Add(new Tuple<int,int> (i,j));
            }
            elementCount += l;
        }
        int[] result = new int[elementCount];
        int count = 0;
        foreach(KeyValuePair<int, List<Tuple<int, int>>> kvp in hashTable)
        {
            List<Tuple<int, int>> lst = kvp.Value;
            lst.Sort();
            lst.Reverse();
            foreach (Tuple<int,int> pair in lst)
            {
                result[count] = nums[pair.Item1][pair.Item2];
                count += 1;
            }
        }       
        return result;
    }
}
// @lc code=end

