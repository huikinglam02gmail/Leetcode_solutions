/*
 * @lc app=leetcode id=1291 lang=cpp
 *
 * [1291] Sequential Digits
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<int> sequentialDigits(int low, int high) {
        std::queue<int> queue;
        std::vector<int> result;

        for (int i = 1; i <= 9; i++) {
            queue.push(i);
        }

        while (!queue.empty()) {
            int num = queue.front();
            queue.pop();

            if (low <= num && num <= high) {
                result.push_back(num);
            }

            if (num <= high && num % 10 < 9) {
                queue.push(num * 10 + (num % 10 + 1));
            }
        }

        std::sort(result.begin(), result.end());
        return result;
    }
};

// @lc code=end

