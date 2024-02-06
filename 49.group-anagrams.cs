/*
 * @lc app=leetcode id=49 lang=csharp
 *
 * [49] Group Anagrams
 */

// @lc code=start
public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> HashTable= new Dictionary<string, List<string>>();
        Dictionary<string, List<string>>.ValueCollection valueColl =
    HashTable.Values;
        string key;
        foreach (string str in strs)
        {
            key = String.Concat(str.OrderBy(c => c));
            if (!HashTable.ContainsKey(key))
            {
                HashTable.Add(key, new List<string>());
            }
            HashTable[key].Add(str);
        }
                
        var result = new List<IList<string>>();
        foreach (List<string> lst in valueColl)
        {
            result.Add(lst);
        }
        return result;
    }
}
// @lc code=end

