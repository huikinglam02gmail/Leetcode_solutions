/*
 * @lc app=leetcode id=2003 lang=cpp
 *
 * [2003] Smallest Missing Genetic Value in Each Subtree
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
private:
    vector<bool> seen;
    vector<vector<int>> children;
    vector<int> nums;

    void DFS(int i) {
        if (!seen[nums[i]]) {
            seen[nums[i]] = true;
            for (int c : children[i]) {
                DFS(c);
            }
        }
    }

public:
    vector<int> smallestMissingValueSubtree(vector<int>& parents, vector<int>& nums) {
        int n = parents.size();
        vector<int> result(n, 1);
        seen = vector<bool>(100001, false);
        seen[0] = true;
        children = vector<vector<int>>(n, vector<int>{});
        this->nums = nums;

        auto indexOfOne = find(nums.begin(), nums.end(), 1);
        if (indexOfOne != nums.end()) {
            int miss = 0;
            for (int i = 0; i < n; i++) {
                if (parents[i] != -1) {
                    children[parents[i]].push_back(i);
                }
            }

            int j = distance(nums.begin(), indexOfOne);
            while (j != -1) {
                DFS(j);
                while (miss < 100001 && seen[miss]) {
                    miss++;
                }
                result[j] = miss;
                j = parents[j];
            }
        }

        return result;
    }
};

// @lc code=end

