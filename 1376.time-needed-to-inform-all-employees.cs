/*
 * @lc app=leetcode id=1376 lang=csharp
 *
 * [1376] Time Needed to Inform All Employees
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    We can BFS from the head to all the leafs
    In each popped out event, we also mark the informed time for this person
    and keep tracking the max time seen
    */
    
    public int NumOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        var subordinates = new List<HashSet<int>>();
        for (int i = 0; i < n; i++) {
            subordinates.Add(new HashSet<int>());
        }
        
        for (int i = 0; i < manager.Length; i++) {
            int person = manager[i];
            if (person != -1) {
                subordinates[person].Add(i);
            }
        }
        
        var queue = new Queue<(int personId, int time)>();
        queue.Enqueue((headID, 0));
        int maxTime = 0;
        
        while (queue.Count > 0) {
            var (personId, time) = queue.Dequeue();
            maxTime = Math.Max(maxTime, time);
            
            foreach (int subordinate in subordinates[personId]) {
                queue.Enqueue((subordinate, time + informTime[personId]));
            }
        }
        
        return maxTime;
    }
}

// @lc code=end

