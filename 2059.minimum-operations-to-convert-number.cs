/*
 * @lc app=leetcode id=2059 lang=csharp
 *
 * [2059] Minimum Operations to Convert Number
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int MinimumOperations(int[] nums, int start, int goal) {
        Queue<int> dq = new Queue<int>();
        HashSet<int> seen = new HashSet<int>();
        dq.Enqueue(start);
        seen.Add(start);
        int steps = 0;
        
        while (dq.Count > 0) {
            int count = dq.Count;
            for (int i = 0; i < count; i++) {
                int node = dq.Dequeue();
                if (node == goal) return steps;
                
                if (node >= 0 && node <= 1000) {
                    foreach (int num in nums) {
                        int nextNode1 = node + num;
                        int nextNode2 = node - num;
                        int nextNode3 = node ^ num;
                        
                        if (!seen.Contains(nextNode1)) {
                            seen.Add(nextNode1);
                            dq.Enqueue(nextNode1);
                        }
                        if (!seen.Contains(nextNode2)) {
                            seen.Add(nextNode2);
                            dq.Enqueue(nextNode2);
                        }
                        if (!seen.Contains(nextNode3)) {
                            seen.Add(nextNode3);
                            dq.Enqueue(nextNode3);
                        }
                    }
                }
            }
            steps++;
        }
        
        return -1;
    }
}

// @lc code=end

