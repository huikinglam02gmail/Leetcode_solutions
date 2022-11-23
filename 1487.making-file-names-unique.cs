/*
 * @lc app=leetcode id=1487 lang=csharp
 *
 * [1487] Making File Names Unique
 */

// @lc code=start
public class Solution 
{
    public string[] GetFolderNames(string[] names) 
    {
        Dictionary<string, int> nextName = new Dictionary<string, int>();
        foreach (string name in names)
        {
            string newName = name;
            if (nextName.ContainsKey(name))
            {
                int nextNameID = nextName[newName];
                while (nextName.ContainsKey(newName))
                {
                    nextNameID++;
                    newName = name + "(" + nextNameID.ToString() + ")";
                }
                nextName[name] = nextNameID;
            }
            nextName[newName] = 0;
        }
        return nextName.Keys.ToArray();
    }
}
// @lc code=end

