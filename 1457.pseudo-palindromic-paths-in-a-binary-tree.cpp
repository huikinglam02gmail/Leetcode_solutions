/*
 * @lc app=leetcode id=1457 lang=cpp
 *
 * [1457] Pseudo-Palindromic Paths in a Binary Tree
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
#include <unordered_set>
#include <tuple>

class Solution
{
public:
    /**
     * Palindromes = even appearance in all or all but 1
     * We can use BFS from root to obtain all root to leaf paths
     * Since the values are only 1-9, we might use bit representation of odd vs even number of occurrence seen in the previous path
     */

    int updateState(int state, int num)
    {
        state ^= (1 << (num - 1));
        return state;
    }

    int pseudoPalindromicPaths(TreeNode *root)
    {
        std::queue<std::tuple<TreeNode *, int>> q;
        int result = 0;
        q.push(std::make_tuple(root, updateState(0, root->val)));
        std::unordered_set<int> palindromes = {0};

        for (int i = 0; i < 9; i++)
        {
            palindromes.insert(1 << i);
        }

        while (!q.empty())
        {
            auto current = q.front();
            q.pop();
            TreeNode *node = std::get<0>(current);
            int state = std::get<1>(current);

            if (!node->left && !node->right && palindromes.count(state))
            {
                result++;
            }

            if (node->left)
            {
                q.push(std::make_tuple(node->left, updateState(state, node->left->val)));
            }

            if (node->right)
            {
                q.push(std::make_tuple(node->right, updateState(state, node->right->val)));
            }
        }

        return result;
    }
};

// @lc code=end

