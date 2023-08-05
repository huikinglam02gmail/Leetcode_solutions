/*
 * @lc app=leetcode id=95 lang=cpp
 *
 * [95] Unique Binary Search Trees II
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
class Solution {
public:
    std::vector<TreeNode*> constructTrees(int start, int end) {
        std::vector<TreeNode*> list;

        if (start > end) {
            list.push_back(nullptr);
            return list;
        }

        for (int i = start; i <= end; i++) {
            std::vector<TreeNode*> leftSubtree = constructTrees(start, i - 1);
            std::vector<TreeNode*> rightSubtree = constructTrees(i + 1, end);

            for (TreeNode* left : leftSubtree) {
                for (TreeNode* right : rightSubtree) {
                    TreeNode* node = new TreeNode(i);
                    node->left = left;
                    node->right = right;
                    list.push_back(node);
                }
            }
        }
        return list;
    }

    std::vector<TreeNode*> generateTrees(int n) {
        return constructTrees(1, n);
    }
};
// @lc code=end

