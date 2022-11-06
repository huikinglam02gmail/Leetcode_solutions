/*
 * @lc app=leetcode id=1436 lang=csharp
 *
 * [1436] Destination City
 */

// @lc code=start
public class Solution {
    public string DestCity(IList<IList<string>> paths) 
    {
        Dictionary<string, int> outgoing = new Dictionary<string, int>();
        foreach (IList<string> row in paths)
        {
            List<string> rowList = row.ToList();
            string start = rowList[0];
            string end = rowList[1];
            if (!outgoing.ContainsKey(start))
            {
                outgoing.Add(start, 0);
            }
            outgoing[start] += 1;
            if (!outgoing.ContainsKey(end))
            {
                outgoing.Add(end, 0);
            }            
        }
        foreach (KeyValuePair<string, int> kvp in outgoing)
        {
            if (kvp.Value == 0)
            {
                return kvp.Key;
            }
        }
        return "";
    }
}
// @lc code=end

