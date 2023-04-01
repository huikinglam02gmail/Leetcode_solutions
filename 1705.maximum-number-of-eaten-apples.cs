/*
 * @lc app=leetcode id=1705 lang=csharp
 *
 * [1705] Maximum Number of Eaten Apples
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    public int EatenApples(int[] apples, int[] days) 
    {
        PriorityQueue<int, int> pq = new PriorityQueue<int, int>();
        int result = 0;
        for (int i = 0; i < apples.Length; i++)
        {
            if (apples[i] > 0)
            {
                pq.Enqueue(apples[i], i + days[i]);
            }
            while (pq.TryPeek(out int apple, out int deadline) && deadline <= i)
            {
                pq.Dequeue();
            }
            if (pq.TryDequeue(out int apple1, out int deadline1))
            {
                result++;
                if (apple1 > 1)
                {
                    pq.Enqueue(apple1 - 1, deadline1);
                }
            }
        }
        int date = apples.Length;
        while (pq.Count > 0)
        {
            while (pq.TryPeek(out int apple2, out int deadline2) && deadline2 <= date)
            {
                pq.Dequeue();
            }
            if (pq.TryDequeue(out int apple3, out int deadline3))
            {
                int canEat = Math.Min(deadline3 - date, apple3);
                result += canEat;
                date += canEat;
            }                        
        }
        return result;
    }
}
// @lc code=end

