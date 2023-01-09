/*
 * @lc app=leetcode id=1604 lang=csharp
 *
 * [1604] Alert Using Same Key-Card Three or More Times in a One Hour Period
 */

// @lc code=start
public class Solution 
{
    SortedDictionary<string, List<int>> hashTable;

    public bool triedThrice(string name)
    {
        for (int i = 2; i < hashTable[name].Count; i++)
        {
            if (hashTable[name][i] - hashTable[name][i - 2] <= 60)
            {
                return true;
            }
        }
        return false;
    }

    public IList<string> AlertNames(string[] keyName, string[] keyTime) 
    {
        hashTable = new SortedDictionary<string, List<int>>();
        List<string> result = new List<string>();
        for (int i = 0; i < keyName.Length; i++)
        {
            if (!hashTable.ContainsKey(keyName[i]))
            {
                hashTable.Add(keyName[i], new List<int>());
            }
            hashTable[keyName[i]].Add(60*Int32.Parse(keyTime[i].Substring(0,2)) + Int32.Parse(keyTime[i].Substring(3,2)));
        }

        foreach (string key in hashTable.Keys)
        {
            hashTable[key].Sort();
            if (triedThrice(key))
            {
                result.Add(key);
            }
        }
        return result;
    }
}
// @lc code=end

