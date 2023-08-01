/*
 * @lc app=leetcode id=77 lang=cpp
 *
 * [77] Combinations
 */

// @lc code=start
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combine(int n, int k) {
        std::vector<std::vector<int>> result;
        std::vector<int> numbers;
        for (int i = 1; i <= n; i++) {
            numbers.push_back(i);
        }
        std::vector<int> current;
        combineHelper(numbers, k, 0, current, result);
        return result;
    }

private:
    void combineHelper(const std::vector<int>& numbers, int k, int start, std::vector<int>& current, std::vector<std::vector<int>>& result) {
        if (k == 0) {
            result.push_back(current);
            return;
        }

        for (int i = start; i < numbers.size(); i++) {
            current.push_back(numbers[i]);
            combineHelper(numbers, k - 1, i + 1, current, result);
            current.pop_back();
        }
    }
};

// @lc code=end

