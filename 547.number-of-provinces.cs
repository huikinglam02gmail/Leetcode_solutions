/*
 * @lc app=leetcode id=547 lang=csharp
 *
 * [547] Number of Provinces
 */

// @lc code=start
using System.Collections.Generic;

public class Solution 
{
    public int FindCircleNum(int[][] isConnected) 
    {
        Queue<int> dq = new Queue<int>();
        HashSet<int> visited = new HashSet<int>();
        int province = 0;
        int n = isConnected.Length;
        
        for (int i = 0; i < n; i++) 
        {
            if (!visited.Contains(i)) 
            {
                dq.Enqueue(i);
                visited.Add(i);
                province++;
                
                while (dq.Count > 0) 
                {
                    int x = dq.Dequeue();
                    
                    for (int j = 0; j < n; j++) {
                        if (isConnected[x][j] == 1 && !visited.Contains(j)) {
                            dq.Enqueue(j);
                            visited.Add(j);
                        }
                    }
                }
            }
        }
        
        return province;
    }
}

// @lc code=end

