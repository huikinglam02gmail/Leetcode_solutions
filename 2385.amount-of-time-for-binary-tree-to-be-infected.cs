/*
 * @lc app=leetcode id=2385 lang=csharp
 *
 * [2385] Amount of Time for Binary Tree to Be Infected
 */

// @lc code=start
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
using System;
using System.Collections.Generic;

public class Solution {
    public int AmountOfTime(TreeNode root, int start) {
        Dictionary<int, HashSet<int>> graph = new Dictionary<int, HashSet<int>>();
        Queue<TreeNode> dq = new Queue<TreeNode>();
        dq.Enqueue(root);

        if (!graph.ContainsKey(root.val)) {
            graph[root.val] = new HashSet<int>();
        }

        while (dq.Count > 0) {
            TreeNode node = dq.Dequeue();

            if (node.left != null) {
                graph[node.val].Add(node.left.val);
                if (!graph.ContainsKey(node.left.val)) {
                    graph[node.left.val] = new HashSet<int>();
                }
                graph[node.left.val].Add(node.val);
                dq.Enqueue(node.left);
            }

            if (node.right != null) {
                graph[node.val].Add(node.right.val);
                if (!graph.ContainsKey(node.right.val)) {
                    graph[node.right.val] = new HashSet<int>();
                }
                graph[node.right.val].Add(node.val);
                dq.Enqueue(node.right);
            }
        }

        int result = -1;
        HashSet<int> visited = new HashSet<int>();
        Queue<int> dq1 = new Queue<int>();
        dq1.Enqueue(start);
        visited.Add(start);

        while (dq1.Count > 0) {
            int count = dq1.Count;
            for (int i = 0; i < count; i++) {
                int node = dq1.Dequeue();
                foreach (int next in graph[node]) {
                    if (!visited.Contains(next)) {
                        visited.Add(next);
                        dq1.Enqueue(next);
                    }
                }
            }
            result++;
        }

        return result;
    }
}

// @lc code=end

