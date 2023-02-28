/*
 * @lc app=leetcode id=652 lang=csharp
 *
 * [652] Find Duplicate Subtrees
 */

// @lc code=start

using System.Collections.Generic;
using System;
using System.Linq;

//Definition for a binary tree node.
//  public class TreeNode 
//  {
//     public int val;
//     public TreeNode left;
//     public TreeNode right;
//     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) 
//     {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
//   }
 
public class Solution 
{
    HashSet<string> seen;
    HashSet<string> result;
    public string serializeBinaryTree(TreeNode node)
    {
        Queue<TreeNode> queue = new Queue<TreeNode>();
        List<string> bfs = new List<string>();
        queue.Enqueue(node);
        while (queue.TryDequeue(out TreeNode node1))
        {
            if (node1 == null)
            {
                bfs.Add("null");
            }
            else
            {
                bfs.Add(node1.val.ToString());
                queue.Enqueue(node1.left);
                queue.Enqueue(node1.right);
            }
        }
        return string.Join(",", bfs.ToArray());
    }

    public TreeNode deserializeBinaryTree(string data)
    {
        if (data.Equals("null", StringComparison.OrdinalIgnoreCase))
        {
            return null;
        }
        else
        {
            string[] strings = data.Split(",");
            TreeNode root = new TreeNode(Int32.Parse(strings[0]));
            Queue<TreeNode> queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            bool left = true;
            TreeNode node = default;
            TreeNode parent = default;            

            for (int i = 1; i < strings.Length; i++)
            {
                if (!strings[i].Equals("null", StringComparison.OrdinalIgnoreCase))
                {
                    node = new TreeNode(Int32.Parse(strings[i]));
                    queue.Enqueue(node);
                }
                else
                {
                    node = null;
                }

                if (left)
                {
                    parent = queue.Dequeue();
                    parent.left = node;
                }
                else
                {
                    parent.right = node;
                }
                left = !left;
            }
            return root;
        }
    }

    public void dfs(TreeNode root)
    {
        if (root.left != null)
        {
            dfs(root.left);
        }
        if (root.right != null)
        {
            dfs(root.right);
        }
        string rootString= serializeBinaryTree(root);

        if (!seen.Contains(rootString))
        {
            seen.Add(rootString);
        }
        else
        {
            result.Add(rootString);
        }
    }

    public IList<TreeNode> FindDuplicateSubtrees(TreeNode root) 
    {
        seen = new HashSet<string>();
        result = new HashSet<string>();
        dfs(root);
        return result.Select(x => deserializeBinaryTree(x)).ToList();
    }
}
// @lc code=end

