/*
 * @lc app=leetcode id=1585 lang=csharp
 *
 * [1585] Check If String Is Transformable With Substring Sort Operations
 */

// @lc code=start
public class Solution 
{
    public bool IsTransformable(string s, string t) 
    {
        List<int>[] appearance = new List<int>[10];
        int[] seenInT = new int[10];
        for (int i = 0; i < 10; i++)
        {
            appearance[i] = new List<int>();
            seenInT[i] = 0;
        }
        for (int i = 0; i < s.Length; i++)
        {
            appearance[s[i] - '0'].Add(i);
        }
        foreach (char c in t)
        {
            if (seenInT[c - '0'] >= appearance[c - '0'].Count)
            {
                return false;
            }
            for (int i = 0; i < c - '0'; i++)
            {
                if (seenInT[i] < appearance[i].Count && appearance[i][seenInT[i]] < appearance[c - '0'][seenInT[c - '0']])
                {
                    return false;
                }
            }
            seenInT[c - '0']++;
        }
        return true;
    }
}
// @lc code=end

