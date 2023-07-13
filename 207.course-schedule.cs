/*
 * @lc app=leetcode id=207 lang=csharp
 *
 * [207] Course Schedule
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        List<List<int>> G = new List<List<int>>();
        int[] degree = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            G.Add(new List<int>());
        }
        
        foreach (int[] prerequisite in prerequisites) {
            int j = prerequisite[0];
            int i = prerequisite[1];
            G[i].Add(j);
            degree[j]++;
        }
        
        Queue<int> dq = new Queue<int>();
        HashSet<int> seen = new HashSet<int>();
        for (int i = 0; i < numCourses; i++)
        {
            if (degree[i] == 0)
            {
                dq.Enqueue(i);
                seen.Add(i);
            }
        }
        
        while (dq.TryDequeue(out int i))
        {
            foreach (int j in G[i])
            {
                degree[j]--;
                if (degree[j] == 0)
                {
                    dq.Enqueue(j);
                    seen.Add(j);
                }
            }
        }
        return seen.Count == numCourses;
    }
}

// @lc code=end

