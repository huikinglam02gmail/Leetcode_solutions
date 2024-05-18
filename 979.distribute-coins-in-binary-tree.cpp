/*
 * @lc app=leetcode id=979 lang=cpp
 *
 * [979] Distribute Coins in Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <cstdlib>  // For abs

class Solution {
private:
    int result;

    // We know the final state: node.val = 1 for all nodes.
    // Now let's think about the "flux" of coins between parent and its children
    // And define that to be the return value of the DFS function
    // If positive: coins will be going back to its parent
    // If negative: coins will be going from its parent    

    int dfs(TreeNode* node) {
        if (node == nullptr) return 0;
        int left = dfs(node->left);
        int right = dfs(node->right);
        result += std::abs(left) + std::abs(right);
        return node->val + left + right - 1;
    }

public:
    int distributeCoins(TreeNode* root) {
        result = 0;
        dfs(root);
        return result;
    }
};

// @lc code=end

