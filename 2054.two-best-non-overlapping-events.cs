/*
 * @lc app=leetcode id=2054 lang=csharp
 *
 * [2054] Two Best Non-Overlapping Events
 */

// @lc code=start
public class Solution {
    public int MaxTwoEvents(int[][] events) {
        events = events.OrderBy(x => x[1]).ToArray();
        PriorityQueue<int, Tuple<int, int>> heap = new PriorityQueue<int, Tuple<int, int>>();
        int result = 0;
        int current = 0;
        foreach (int[] evnt in events) {
            heap.Enqueue(evnt[0], new Tuple<int, int>(-evnt[2], evnt[0]));
        }
        foreach (int[] evnt in events){
            while (heap.TryPeek(out int s, out Tuple<int, int> t)  && t.Item2 <= evnt[1]) heap.Dequeue();
            current = evnt[2];
            if (heap.TryPeek(out int s1, out Tuple<int, int> t1)) current -= t1.Item1;
            result = Math.Max(result, current);
        }
        return result;
    }
}
// @lc code=end

