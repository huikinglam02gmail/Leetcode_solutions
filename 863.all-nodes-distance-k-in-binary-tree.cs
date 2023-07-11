/*
 * @lc app=leetcode id=863 lang=csharp
 *
 * [863] All Nodes Distance K in Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public IList<int> DistanceK(TreeNode root, TreeNode target, int k) {
        Dictionary<int, HashSet<int>> graph = new Dictionary<int, HashSet<int>>();
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        graph[root.val] = new HashSet<int>();

        while (queue.Count > 0) {
            TreeNode node = queue.Dequeue();

            if (node.left != null) {
                graph[node.left.val] = new HashSet<int>();
                graph[node.val].Add(node.left.val);
                graph[node.left.val].Add(node.val);
                queue.Enqueue(node.left);
            }

            if (node.right != null) {
                graph[node.right.val] = new HashSet<int>();
                graph[node.val].Add(node.right.val);
                graph[node.right.val].Add(node.val);
                queue.Enqueue(node.right);
            }
        }

        Queue<int> dq = new Queue<int>();
        HashSet<int> visited = new HashSet<int>();
        dq.Enqueue(target.val);
        visited.Add(target.val);
        int steps = 0;
        List<int> result = new List<int>();

        while (dq.Count > 0) {
            int count = dq.Count;

            for (int i = 0; i < count; i++) {
                int node = dq.Dequeue();

                if (steps == k) {
                    result.Add(node);
                }
                else {
                    foreach (int next in graph[node]) {
                        if (!visited.Contains(next)) {
                            visited.Add(next);
                            dq.Enqueue(next);
                        }
                    }
                }
            }

            if (steps == k) {
                return result;
            }

            steps++;
        }

        return result;
    }
}
// @lc code=end

