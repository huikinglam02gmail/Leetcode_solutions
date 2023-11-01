/*
 * @lc app=leetcode id=501 lang=csharp
 *
 * [501] Find Mode in Binary Search Tree
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
public class Solution {
    private int lastNum;
    private int lastCount;
    private int modeCount;
    private List<int> modeList;

    public Solution() {
        lastNum = -100001;
        lastCount = 0;
        modeCount = 0;
        modeList = new List<int>();
    }

    public void Dfs(TreeNode node) {
        if (node.left != null) {
            Dfs(node.left);
        }

        if (node.val == lastNum) {
            lastCount++;
        }
        else {
            lastNum = node.val;
            lastCount = 1;
        }

        if (modeCount == lastCount) {
            modeList.Add(lastNum);
        }
        else if (modeCount < lastCount) {
            modeList.Clear();
            modeCount = lastCount;
            modeList.Add(lastNum);
        }

        if (node.right != null) {
            Dfs(node.right);
        }
    }

    public int[] FindMode(TreeNode root) {
        if (root == null) {
            return new int[0];
        }

        Dfs(root);
        return modeList.ToArray();
    }
}

// @lc code=end

