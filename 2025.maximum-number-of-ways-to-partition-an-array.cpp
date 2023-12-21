/*
 * @lc app=leetcode id=2025 lang=cpp
 *
 * [2025] Maximum Number of Ways to Partition an Array
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
public:
    int waysToPartition(vector<int>& nums, int k) {
        int n = nums.size();
        int result = 0;
        vector<long> prefixSum(n, 0);
        vector<long> suffixSum(n, 0);

        for (int i = 0; i < n; i++) {
            prefixSum[i] = nums[i];
            suffixSum[i] = nums[i];
        }

        for (int i = 1; i < n; i++) {
            prefixSum[i] += prefixSum[i - 1];
        }

        unordered_map<long, queue<int>> left;
        unordered_map<long, queue<int>> right;

        for (int i = n - 2; i >= 0; i--) {
            suffixSum[i] += suffixSum[i + 1];
            if (suffixSum[i + 1] == prefixSum[i]) {
                result += 1;
            }

            long diff = prefixSum[i] - suffixSum[i + 1];
            right[diff].push(i);
        }

        for (int i = 0; i < n; i++) {
            int current = (left.count(k - nums[i]) ? left[k - nums[i]].size() : 0) +
                          (right.count(nums[i] - k) ? right[nums[i] - k].size() : 0);

            result = max(result, current);

            if (i < n - 1) {
                long diff = prefixSum[i] - suffixSum[i + 1];
                right[diff].pop();

                if (!left.count(diff)) {
                    left[diff] = queue<int>();
                }

                left[diff].push(i);
            }
        }

        return result;
    }
};

// @lc code=end

