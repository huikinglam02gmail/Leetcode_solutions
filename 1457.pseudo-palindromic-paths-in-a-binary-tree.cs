/*
 * @lc app=leetcode id=1457 lang=csharp
 *
 * [1457] Pseudo-Palindromic Paths in a Binary Tree
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

public class Solution
{
    /**
     * Palindromes = even appearance in all or all but 1
     * We can use BFS from root to obtain all root to leaf paths
     * Since the values are only 1-9, we might use bit representation of odd vs even number of occurrence seen in the previous path
     */

    private int UpdateState(int state, int num)
    {
        state ^= (1 << (num - 1));
        return state;
    }

    public int PseudoPalindromicPaths(TreeNode root)
    {
        Queue<Tuple<TreeNode, int>> queue = new Queue<Tuple<TreeNode, int>>();
        int result = 0;
        queue.Enqueue(new Tuple<TreeNode, int>(root, UpdateState(0, root.val)));
        HashSet<int> palindromes = new HashSet<int> { 0 };

        for (int i = 0; i < 9; i++)
        {
            palindromes.Add(1 << i);
        }

        while (queue.Count > 0)
        {
            Tuple<TreeNode, int> current = queue.Dequeue();
            TreeNode node = current.Item1;
            int state = current.Item2;

            if (node.left == null && node.right == null && palindromes.Contains(state))
            {
                result++;
            }

            if (node.left != null)
            {
                queue.Enqueue(new Tuple<TreeNode, int>(node.left, UpdateState(state, node.left.val)));
            }

            if (node.right != null)
            {
                queue.Enqueue(new Tuple<TreeNode, int>(node.right, UpdateState(state, node.right.val)));
            }
        }

        return result;
    }
}


// @lc code=end

