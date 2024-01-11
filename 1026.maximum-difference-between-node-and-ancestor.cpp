/*
 * @lc app=leetcode id=1026 lang=cpp
 *
 * [1026] Maximum Difference Between Node and Ancestor
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
#include <algorithm>
#include <cmath>

class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        int ans = 0;
        dfs(root, ans);
        return ans;
    }

    std::pair<int, int> dfs(TreeNode* root, int& ans) {
        if (!root) {
            return {INT_MAX, INT_MIN};
        }

        auto leftMinMax = dfs(root->left, ans);
        auto rightMinMax = dfs(root->right, ans);

        int nodeMin = std::min({root->val, leftMinMax.first, rightMinMax.first});
        int nodeMax = std::max({root->val, leftMinMax.second, rightMinMax.second});

        ans = std::max(ans, std::max(std::abs(root->val - nodeMin), std::abs(root->val - nodeMax)));

        return {nodeMin, nodeMax};
    }
};

// @lc code=end

