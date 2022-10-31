/*
 * @lc app=leetcode id=1425 lang=csharp
 *
 * [1425] Constrained Subsequence Sum
 */

// @lc code=start
public class Solution {
    public int ConstrainedSubsetSum(int[] nums, int k) {
        int result = Int32.MinValue;
        int n = nums.Length;
        PriorityQueue<int, int> heap = new PriorityQueue<int, int>();
        for (int i = 0; i < n; i++)
        {
            while (heap.Count > 0 && i - heap.Peek() > k)
            {
                heap.Dequeue();
            }

            int maxsofar = 0;
            if (heap.TryPeek(out int ind, out int maxseen))
            {
                maxsofar = Math.Max(maxsofar, - maxseen);
            }
            result = Math.Max(result, nums[i] + maxsofar);
            heap.Enqueue(i, -nums[i]-maxsofar);
        }
        return result;
    }
}
// @lc code=end

