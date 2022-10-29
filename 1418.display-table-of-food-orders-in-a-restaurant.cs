/*
 * @lc app=leetcode id=1418 lang=csharp
 *
 * [1418] Display Table of Food Orders in a Restaurant
 */

// @lc code=start
public class Solution {
    public IList<IList<string>> DisplayTable(IList<IList<string>> orders) {
        Dictionary<(string, string),int> hashTable = new Dictionary<(string, string),int>();
        List<IList<string>> result = new List<IList<string>>();
        SortedSet<int> tables = new SortedSet<int>();
        SortedSet<string> food = new SortedSet<string>(StringComparer.Ordinal);
        
        foreach (IList<string> lst in orders)
        {
            (string, string) key = (lst[1], lst[2]);
            tables.Add(Int32.Parse(lst[1]));
            food.Add(lst[2]);
            if (hashTable.TryGetValue(key, out int value))
            {
                hashTable[key] = value;
            }
            else
            {
                hashTable.Add(key, 0);
            }
            hashTable[key] += 1;
        }
        List<int> tableList = tables.ToList();
        List<string> foodList = food.ToList();
        int m = tableList.Count;
        int n = foodList.Count;  
        for (int i = 0; i < m+1; i++)
        {
            result.Add(new List<string>());
            for (int j = 0; j < n+1; j++)
            {
                if (i == 0 && j == 0)
                {
                    result[i].Add("Table");
                }
                else if (i == 0)
                {
                    result[i].Add(foodList[j-1]);
                }
                else if (j == 0)
                {
                    result[i].Add(tableList[i-1].ToString());                 
                }
                else
                {
                    (string, string) key = ((tableList[i-1]).ToString(), foodList[j-1].ToString());
                    if (hashTable.TryGetValue(key, out int value))
                    {
                        result[i].Add(value.ToString());
                    }
                    else
                    {
                        result[i].Add("0");
                    }
                }
            }
        }
        return result;
    }
}
// @lc code=end

