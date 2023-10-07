/*
 * @lc app=leetcode id=1932 lang=csharp
 *
 * [1932] Merge BSTs to Create Single BST
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
using System.Collections.Generic;

public class BSTQueueNode
{
    public TreeNode current;
    public TreeNode leftParent;
    public TreeNode rightParent;
    public int minimum;
    public int maximum;
    public BSTQueueNode(TreeNode current, TreeNode leftParent, TreeNode rightParent, int minimum, int maximum)
    {
        this.current = current;
        this.leftParent = leftParent;
        this.rightParent = rightParent;
        this.minimum = minimum;
        this.maximum = maximum;
    }
}
public class Solution 
{
    HashSet<int> rootValSet;
    public TreeNode CanMerge(IList<TreeNode> trees) 
    {
        if (trees.Count == 1) {
            return trees[0];
        }

        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        rootValSet = new HashSet<int>();

        for (int i = 0; i < trees.Count; i++) {
            hashTable[trees[i].val] = i;
            rootValSet.Add(trees[i].val);
        }

        foreach (var tree in trees) {
            LeafValInHashTable(tree);
        }

        if (rootValSet.Count == 1) 
        {
            int rootVal = 0;
            foreach (var nodeVal in rootValSet) 
            {
                rootVal = nodeVal;
            }
            TreeNode root = trees[hashTable[rootVal]];
            Queue<BSTQueueNode> dq = new Queue<BSTQueueNode>();
            dq.Enqueue(new BSTQueueNode( root, null, null, 0, 50001 ));

            while (dq.TryDequeue(out BSTQueueNode nodeInfo)) {
                TreeNode node = nodeInfo.current;
                TreeNode leftParent = nodeInfo.leftParent;
                TreeNode rightParent = nodeInfo.rightParent;
                int minimum = nodeInfo.minimum;
                int maximum = nodeInfo.maximum;

                if (node.left != null) {
                    dq.Enqueue(new BSTQueueNode ( node.left, null, node, minimum, node.val ));
                }
                if (node.right != null) {
                    dq.Enqueue(new BSTQueueNode ( node.right, node, null, node.val, maximum ));
                }

                if (node.left == null && node.right == null && hashTable.ContainsKey(node.val)) {
                    TreeNode candidate = trees[hashTable[node.val]];
                    if (candidate.right != null && candidate.right.val >= maximum) {
                        continue;
                    }
                    if (candidate.left != null && candidate.left.val <= minimum) {
                        continue;
                    }

                    if (leftParent != null) 
                    {
                        leftParent.right = candidate;
                        dq.Enqueue(new BSTQueueNode ( candidate, leftParent, null, leftParent.val, maximum ));
                    }
                    if (rightParent != null) 
                    {
                        rightParent.left = candidate;
                        dq.Enqueue(new BSTQueueNode ( candidate, null, rightParent, minimum, rightParent.val ));
                    }
                    hashTable.Remove(node.val);
                }
            }

            if (hashTable.Count == 1) 
            {
                foreach (var kvp in hashTable) 
                {
                    return trees[kvp.Value];
                }
            }
        }

        return null;
    }

    private void LeafValInHashTable(TreeNode node) 
    {
        if (node.left != null) {
            LeafValInHashTable(node.left);
        }
        if (node.right != null) {
            LeafValInHashTable(node.right);
        }
        if (node.left == null && node.right == null && rootValSet.Contains(node.val)) 
        {
            rootValSet.Remove(node.val);
        }
    }
}

// @lc code=end

