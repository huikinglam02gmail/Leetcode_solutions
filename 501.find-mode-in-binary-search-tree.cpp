/*
 * @lc app=leetcode id=501 lang=cpp
 *
 * [501] Find Mode in Binary Search Tree
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
#include <vector>

using namespace std;

class Solution {
public:
    int lastNum;
    int lastCount;
    int modeCount;
    vector<int> modeList;

    Solution() {
        lastNum = -100001;
        lastCount = 0;
        modeCount = 0;
    }

    void Dfs(TreeNode* node) {
        if (node->left) {
            Dfs(node->left);
        }

        if (node->val == lastNum) {
            lastCount++;
        }
        else {
            lastNum = node->val;
            lastCount = 1;
        }

        if (modeCount == lastCount) {
            modeList.push_back(lastNum);
        }
        else if (modeCount < lastCount) {
            modeList.clear();
            modeCount = lastCount;
            modeList.push_back(lastNum);
        }

        if (node->right) {
            Dfs(node->right);
        }
    }

    vector<int> findMode(TreeNode* root) {
        if (!root) {
            return vector<int>();
        }

        Dfs(root);
        return modeList;
    }
};

// @lc code=end

