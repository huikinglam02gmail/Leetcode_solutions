/*
 * @lc app=leetcode id=373 lang=csharp
 *
 * [373] Find K Pairs with Smallest Sums
 */

// @lc code=start
public class Solution {
    public IList<IList<int>> KSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<Tuple<int, int>, int> heap = new PriorityQueue<Tuple<int, int>, int>();
        int n1 = nums1.Length;
        int n2 = nums2.Length;
        Tuple<int, int> newTuple;
        HashSet<Tuple<int, int>> visited = new HashSet<Tuple<int, int>>();
        List<IList<int>> result =  new List<IList<int>>();

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
            result.Add(new List<int>() {nums1[t.Item1], nums2[t.Item2]});
        }
        return result;
    }
}
// @lc code=end

