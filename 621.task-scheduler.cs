/*
 * @lc app=leetcode id=621 lang=csharp
 *
 * [621] Task Scheduler
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        Dictionary<char, int> taskCounts = new Dictionary<char, int>();
        foreach (char task in tasks) {
            if (!taskCounts.ContainsKey(task)) {
                taskCounts[task] = 0;
            }
            taskCounts[task]++;
        }
        
        PriorityQueue<int, int> maxHeap = new PriorityQueue<int, int>();
        foreach (var kvp in taskCounts) {
            maxHeap.Enqueue(0, - kvp.Value);
        }
        
        Queue<int[]> queue = new Queue<int[]>();
        int time = 0;
        
        while (queue.Count > 0 || maxHeap.Count > 0) {
            while (queue.Count > 0 && queue.Peek()[1] <= time) {
                int[] item = queue.Dequeue();
                maxHeap.Enqueue(item[1], item[0]);
            }
            
            if (maxHeap.TryDequeue(out int t, out int negCount)) {
                if (negCount < -1) {
                    negCount++;
                    t += n + 1;
                    queue.Enqueue(new int[2]{negCount, t});
                }
            }
            time++;
        }
        
        return time;
    }
}
// @lc code=end

