/*
 * @lc app=leetcode id=1125 lang=csharp
 *
 * [1125] Smallest Sufficient Team
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] SmallestSufficientTeam(string[] reqSkills, IList<IList<string>> people) {
        Dictionary<string, int> skillSet = new Dictionary<string, int>();
        int ns = reqSkills.Length;

        for (int i = 0; i < ns; i++) {
            skillSet[reqSkills[i]] = i;
        }

        Dictionary<int, List<int>> dp = new Dictionary<int, List<int>>();
        dp[0] = new List<int>();

        for (int i = 0; i < people.Count; i++) {
            int peopleMask = 0;

            foreach (var skill in people[i]) {
                peopleMask ^= (1 << skillSet[skill]);
            }

            foreach (var kvp in new List<KeyValuePair<int, List<int>>>(dp)) {
                int skillMask = kvp.Key;
                List<int> team = kvp.Value;
                int newMask = skillMask | peopleMask;

                if (!dp.ContainsKey(newMask) || dp[newMask].Count > 1 + team.Count) {
                    dp[newMask] = new List<int>(team);
                    dp[newMask].Add(i);
                }
            }
        }

        return dp[(1 << ns) - 1].ToArray();
    }
}

// @lc code=end

