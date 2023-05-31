/*
 * @lc app=leetcode id=1733 lang=csharp
 *
 * [1733] Minimum Number of People to Teach
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int MinimumTeachings(int n, int[][] languages, int[][] friendships)
    {
        HashSet<int>[] lang = new HashSet<int>[languages.Length];
        for (int i = 0; i < languages.Length; i++)
        {
            lang[i] = new HashSet<int>(languages[i]);
        }

        List<int[]> frds = new List<int[]>();
        foreach (int[] friendship in friendships)
        {
            int u = friendship[0] - 1;
            int v = friendship[1] - 1;
            bool hasCommonLanguage = false;
            foreach (int language in lang[u])
            {
                if (lang[v].Contains(language))
                {
                    hasCommonLanguage = true;
                    break;
                }
            }
            if (!hasCommonLanguage)
            {
                frds.Add(friendship);
            }
        }

        int result = int.MaxValue;
        for (int i = 1; i <= n; i++)
        {
            HashSet<int> teach = new HashSet<int>();
            foreach (int[] friendship in frds)
            {
                int u = friendship[0] - 1;
                int v = friendship[1] - 1;
                if (!lang[u].Contains(i))
                {
                    teach.Add(u);
                }
                if (!lang[v].Contains(i))
                {
                    teach.Add(v);
                }
            }
            result = Math.Min(result, teach.Count);
        }

        return result;
    }
}

// @lc code=end

