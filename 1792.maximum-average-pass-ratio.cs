/*
 * @lc app=leetcode id=1792 lang=csharp
 *
 * [1792] Maximum Average Pass Ratio
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public double MaxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<int[], double> priorityQueue = new PriorityQueue<int[], double>();
        int n = classes.Length;
        foreach(int[] cl in classes) 
        {
            priorityQueue.Enqueue(cl, ((double)cl[0] / (double)cl[1] - (double)(cl[0] + 1) / (double)(cl[1] + 1)));
        }
        for (int j = extraStudents; j > 0; j--)
        {
            int[] cl = priorityQueue.Dequeue();
            priorityQueue.Enqueue(new int[2]{cl[0] + 1, cl[1] + 1}, ((double)(cl[0] + 1) / (double)(cl[1] + 1) - (double)(cl[0] + 2) / (double)(cl[1] + 2)));
        }

        double result = 0;
        while (priorityQueue.TryDequeue(out int[] cl, out double r))
        {
            result += (double)cl[0] / (double)cl[1];
        }
        return result / (double)n;
    }
}
// @lc code=end

