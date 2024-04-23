/*
 * @lc app=leetcode id=2096 lang=csharp
 *
 * [2096] Step-By-Step Directions From a Binary Tree Node to Another
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
    public string GetDirections(TreeNode r, int sV, int dV) {
        StringBuilder sp = new StringBuilder();
        StringBuilder dp = new StringBuilder();
        GetPath(r, sV, sp);
        GetPath(r, dV, dp);
        
        sp = new StringBuilder(new string(sp.ToString().Reverse().ToArray()));
        dp = new StringBuilder(new string(dp.ToString().Reverse().ToArray()));
        
        while (sp.Length > 0 && dp.Length > 0 && sp[0] == dp[0]) {
            sp.Remove(0, 1);
            dp.Remove(0, 1);
        }
        
        for (int i = 0; i < sp.Length; ++i) {
            if (sp[i] == 'L' || sp[i] == 'R') sp[i] = 'U';
        }
        
        return sp.ToString() + dp.ToString();
    }
    
    public bool GetPath(TreeNode r, int v, StringBuilder p) {
        if (r.val == v) {
            return true;
        } else if (r.left != null && GetPath(r.left, v, p)) {
            p.Append("L");
            return true;
        } else if (r.right != null && GetPath(r.right, v, p)) {
            p.Append("R");
            return true;
        } else {
            return false;
        }
    }
}
// @lc code=end

