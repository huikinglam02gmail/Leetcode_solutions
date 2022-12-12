/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution 
{
    public int CountPairs(TreeNode root, int distance) 
    {
        Queue<Tuple<TreeNode, int>> queue = new Queue<Tuple<TreeNode, int>>();
        Queue<int> queue2 = new Queue<int>();
        HashSet<int> leaves = new HashSet<int>();
        HashSet<int> visited = new HashSet<int>();
        Dictionary<int, HashSet<int>> graph = new Dictionary<int, HashSet<int>>();

        queue.Enqueue(new Tuple<TreeNode, int>(root, 0));
        graph[0] = new HashSet<int>();
        while (queue.TryDequeue(out Tuple<TreeNode, int> t))
        {
            TreeNode node = t.Item1;
            int ind = t.Item2;
            if (node.left == null && node.right == null)
            {
                leaves.Add(ind);
            }
            if (node.left != null)
            {
                int j = 2*ind + 1;
                graph[ind].Add(j);
                graph[j] = new HashSet<int>();
                graph[j].Add(ind);
                queue.Enqueue(new Tuple<TreeNode, int>(node.left, j));
            }
            if (node.right != null)
            {
                int j = 2*ind + 2;
                graph[ind].Add(j);
                graph[j] = new HashSet<int>();
                graph[j].Add(ind);
                queue.Enqueue(new Tuple<TreeNode, int>(node.right, j));
            }
        }
        int result = 0;
        foreach (int leaf in leaves)
        {
            queue2.Clear();
            visited.Clear();
            queue2.Enqueue(leaf);
            visited.Add(leaf);
            int steps = 0;
            while (steps <= distance && queue2.Count() > 0)
            {
                int n = queue2.Count();
                for (int i  = 0; i < n; i++)
                {
                    int item = queue2.Dequeue();
                    if (item != leaf && leaves.Contains(item))
                    {
                        result++;
                    }
                    foreach (int nxt in graph[item])
                    {
                        if (!visited.Contains(nxt))
                        {
                            queue2.Enqueue(nxt);
                            visited.Add(nxt);
                        }
                    }
                }
                steps++;
            }
        }
        return result / 2;
    }
}
// @lc code=end

