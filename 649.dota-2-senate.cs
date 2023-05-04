/*
 * @lc app=leetcode id=649 lang=csharp
 *
 * [649] Dota2 Senate
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public string PredictPartyVictory(string senate) 
    {
        Queue<int> R = new Queue<int>();
        Queue<int> D = new Queue<int>();
        int n = senate.Length;
        for (int i = 0; i < n; i++)
        {
            if (senate[i] == 'R')
            {
                R.Enqueue(i);
            }
            else
            {
                D.Enqueue(i);                
            }
        }
        while (R.Count > 0 && D.Count > 0)
        {
            int r = R.Dequeue();
            int d = D.Dequeue();
            if (r > d)
            {
                D.Enqueue(d + n);
            }
            else
            {
                R.Enqueue(r + n);                
            }
        }
        return R.Count > 0 ? "Radiant" : "Dire";
    }
}
// @lc code=end

