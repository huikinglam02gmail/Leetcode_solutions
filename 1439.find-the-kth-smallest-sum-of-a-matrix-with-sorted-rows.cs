/*
 * @lc app=leetcode id=1439 lang=csharp
 *
 * [1439] Find the Kth Smallest Sum of a Matrix With Sorted Rows
 */

// @lc code=start
public class Solution {
    public List<int> KSmallestPairs(int[] nums1, int[] nums2, int k)
    {
        PriorityQueue<Tuple<int, int>, int> heap = new PriorityQueue<Tuple<int, int>, int>();
        int n1 = nums1.Length;
        int n2 = nums2.Length;
        Tuple<int, int> newTuple;
        HashSet<Tuple<int, int>> visited = new HashSet<Tuple<int, int>>();
        List<int> result =  new List<int>();

        heap.Enqueue(new Tuple<int,int> (0, 0), nums1[0] + nums2[0]);
        visited.Add(new Tuple<int,int> (0, 0));


        while (result.Count < k && heap.TryDequeue(out Tuple<int, int> t, out int total))
        {
            newTuple = new Tuple<int,int> (t.Item1+1, t.Item2);
            if (t.Item1 < n1 - 1 && !visited.Contains(newTuple))
            {
                heap.Enqueue(newTuple, total - nums1[t.Item1] + nums1[t.Item1+1]);
                visited.Add(newTuple);
            }
            newTuple = new Tuple<int,int> (t.Item1, t.Item2+1);
            if (t.Item2 < n2 - 1 && !visited.Contains(newTuple))
            {
                heap.Enqueue(newTuple, total - nums2[t.Item2] + nums2[t.Item2+1]);
                visited.Add(newTuple);
            }
            result.Add(nums1[t.Item1] + nums2[t.Item2]);
        }
        return result;
    }
    public int KthSmallest(int[][] mat, int k) {
        int m = mat.Length;
        List<int> pairs = mat[0].ToList();

        for (int i = 0; i < m-1; i++)
        {
            pairs = KSmallestPairs(pairs.ToArray(), mat[i+1], 200);
        }
        return pairs[k - 1];
    }
}
// @lc code=end

