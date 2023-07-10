/*
 * @lc app=leetcode id=111 lang=cpp
 *
 * [111] Minimum Depth of Binary Tree
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
#include<queue>
using std::queue;
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        
        queue<TreeNode*> q {};
        q.push(root);
        int steps = 1;
        
        while (q.size() > 0) {
            int levelSize = q.size();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();

                if (node -> left == NULL && node -> right == NULL) {
                    return steps;
                }
                
                if (node -> left != NULL) {
                    q.push(node -> left);
                }
                
                if (node -> right != NULL) {
                    q.push(node -> right);
                }
            }
            
            steps++;
        }
        
        return -1;
    }
};
// @lc code=end

