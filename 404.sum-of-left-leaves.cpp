/*
 * @lc app=leetcode id=404 lang=cpp
 *
 * [404] Sum of Left Leaves
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
#include <queue>
using namespace std;

class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == nullptr)
            return 0;
        
        queue<TreeNode*> q;
        q.push(root);
        int result = 0;
        
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if (node->left != nullptr) {
                q.push(node->left);
                if (node->left->left == nullptr && node->left->right == nullptr)
                    result += node->left->val;
            }
            if (node->right != nullptr)
                q.push(node->right);
        }
        
        return result;
    }
};

// @lc code=end

