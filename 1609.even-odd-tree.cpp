/*
 * @lc app=leetcode id=1609 lang=cpp
 *
 * [1609] Even Odd Tree
 */

// @lc code=start
#include <queue>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        if (!root) return true;
        
        int level = 0;
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int prev = level % 2 == 0 ? 0 : 1000001;
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                
                if ((level % 2 == 0 && (node->val <= prev || node->val % 2 == 0)) ||
                    (level % 2 == 1 && (node->val >= prev || node->val % 2 == 1))) {
                    return false;
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
                
                prev = node->val;
            }
            
            ++level;
        }
        
        return true;
    }
};

// @lc code=end

