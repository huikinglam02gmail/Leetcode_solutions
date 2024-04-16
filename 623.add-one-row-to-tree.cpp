/*
 * @lc app=leetcode id=623 lang=cpp
 *
 * [623] Add One Row to Tree
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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) return new TreeNode(val, root, nullptr);
        
        queue<TreeNode*> q;
        int currentDepth = 1;
        q.push(root);
        
        while (currentDepth < depth) {
            currentDepth++;
            int levelSize = q.size();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (currentDepth == depth) {
                    TreeNode* leftNode = node->left;
                    TreeNode* rightNode = node->right;
                    node->left = new TreeNode(val);
                    node->left->left = leftNode;
                    node->right = new TreeNode(val);
                    node->right->right = rightNode;
                } else {
                    if (node->left != nullptr)
                        q.push(node->left);
                    if (node->right != nullptr)
                        q.push(node->right);
                }
            }
        }
        
        return root;
    }
};

// @lc code=end

