/*
 * @lc app=leetcode id=1161 lang=cpp
 *
 * [1161] Maximum Level Sum of a Binary Tree
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
using std::queue;

class Solution {
public:
    int maxLevelSum(TreeNode* root) 
    {
        queue<TreeNode*> q {};
        int level = 1;
        int maxLevel = -1;
        int maxSoFar = INT_MIN;
        q.push(root);

        while (q.size() > 0)
        {
            int total = 0;
            int queueLength = q.size();

            for (int i = 0; i < queueLength; i++)
            {
                TreeNode* node = q.front();
                q.pop();
                total += node->val;

                if (node->left != nullptr)
                    q.push(node->left);

                if (node->right != nullptr)
                    q.push(node->right);
            }

            if (total > maxSoFar)
            {
                maxLevel = level;
                maxSoFar = total;
            }

            level++;
        }

        return maxLevel;    
    }
};
// @lc code=end

