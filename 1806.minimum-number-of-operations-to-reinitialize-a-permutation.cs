/*
 * @lc app=leetcode id=1806 lang=csharp
 *
 * [1806] Minimum Number of Operations to Reinitialize a Permutation
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    We can use BFS from each index and find all the possible positions. The result is the maximum cluster size.
    */
    public int ReinitializePermutation(int n) {
        bool[] seen = new bool[n];
        int result = 0;
        
        for (int i = 0; i < n; i++) {
            if (!seen[i]) {
                Queue<int> dq = new Queue<int>();
                seen[i] = true;
                dq.Enqueue(i);
                int ans = 0;
                
                while (dq.TryDequeue(out int node)) {
                    ans++;
                    int nxt = (node % 2 == 0) ? node / 2 : n / 2 + (node - 1) / 2;
                    
                    if (!seen[nxt]) {
                        seen[nxt] = true;
                        dq.Enqueue(nxt);
                    }
                }
                
                result = Math.Max(result, ans);
            }
        }
        
        return result;
    }
}

// @lc code=end

