/*
 * @lc app=leetcode id=2035 lang=cpp
 *
 * [2035] Partition Array Into Two Arrays to Minimize Sum Difference
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <unordered_set>

using std::lower_bound;
using std::vector;

class Solution {
private:
    std::vector<std::vector<int>> SubSetSums(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<std::vector<int>> sums;

        for (int i = 0; i <= n; i++) {
            std::unordered_set<int> s;
            vector<vector<int>> indicesList = Combine(n, i);
            for (vector<int> indices : indicesList)
            {
                int current = 0;
                for (int ind : indices) current += nums[ind];
                s.insert(current);
            }

            sums.push_back(std::vector<int>(s.begin(), s.end()));
            std::sort(sums.back().begin(), sums.back().end());
        }

        return sums;
    }

    void CombineHelper(const std::vector<int>& numbers, int k, int start, std::vector<int>& current, std::vector<std::vector<int>>& result) {
        if (k == 0) {
            result.push_back(current);
            return;
        }

        for (int i = start; i < numbers.size(); i++) {
            current.push_back(numbers[i]);
            CombineHelper(numbers, k - 1, i + 1, current, result);
            current.pop_back();
        }
    }

public:
    std::vector<std::vector<int>> Combine(int n, int k) {
        std::vector<int> numbers(n);
        std::iota(numbers.begin(), numbers.end(), 0);

        std::vector<std::vector<int>> result;
        std::vector<int> current;

        CombineHelper(numbers, k, 0, current, result);

        return result;
    }

    int minimumDifference(const std::vector<int>& nums) {
        int n = nums.size() / 2;
        std::vector<int> left(nums.begin(), nums.begin() + n);
        std::vector<int> right(nums.begin() + n, nums.end());

        std::vector<std::vector<int>> leftSums = SubSetSums(left);
        std::vector<std::vector<int>> rightSums = SubSetSums(right);

        int S = std::accumulate(nums.begin(), nums.end(), 0);
        int target = S / 2;
        int result = INT_MAX;

        for (int i = 0; i <= n; i++) {
            for (int s : leftSums[i]) {
                int ind = lower_bound(rightSums[n - i].begin(), rightSums[n - i].end(), target - s) - rightSums[n - i].begin();
                if (0 <= ind && ind < rightSums[n - i].size()) result = std::min(result, std::abs(2 * (rightSums[n - i][ind] + s) - S));
                if (0 <= ind - 1 && ind - 1 < rightSums[n - i].size()) result = std::min(result, std::abs(2 * (rightSums[n - i][ind - 1] + s) - S));
                if (0 <= ind + 1 && ind + 1 < rightSums[n - i].size()) result = std::min(result, std::abs(2 * (rightSums[n - i][ind + 1] + s) - S));
            }
        }

        return result;
    }
};

// @lc code=end

