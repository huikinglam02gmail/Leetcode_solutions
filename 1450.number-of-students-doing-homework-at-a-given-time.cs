/*
 * @lc app=leetcode id=1450 lang=csharp
 *
 * [1450] Number of Students Doing Homework at a Given Time
 */

// @lc code=start
public class Solution 
{   
    public int BusyStudent(int[] startTime, int[] endTime, int queryTime) 
    {
        PriorityQueue<int, int> heap = new PriorityQueue<int, int>();
        for (int i = 0; i < startTime.Length; i++)
        {
            int start = startTime[i];
            int end = endTime[i];
            heap.Enqueue(1, start);
            heap.Enqueue(-1, end + 1);
        }

        int active = 0;
        while (heap.TryPeek(out int status, out int time) && time <= queryTime)
        {
            status = heap.Dequeue();
            if (status > 0)
            {
                active++;
            }
            else
            {
                active--;
            }
        }
        return active;
    }
}
// @lc code=end

