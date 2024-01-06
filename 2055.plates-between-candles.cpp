/*
 * @lc app=leetcode id=2055 lang=cpp
 *
 * [2055] Plates Between Candles
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> platesBetweenCandles(std::string s, std::vector<std::vector<int>>& queries) {
        std::vector<int> candles;
        std::vector<int> platesBeforeCandle;
        int plateCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '*') {
                plateCount++;
            } else {
                candles.push_back(i);
                platesBeforeCandle.push_back(plateCount);
            }
        }

        std::vector<int> result;

        for (const auto& query : queries) {
            int l = query[0];
            int r = query[1];

            auto leftCandleIter = std::lower_bound(candles.begin(), candles.end(), l);
            auto rightCandleIter = std::upper_bound(candles.begin(), candles.end(), r);

            int leftCandleIndex = leftCandleIter - candles.begin();
            int rightCandleIndex = rightCandleIter - candles.begin();
            rightCandleIndex -= 1;

            int current = 0;

            if (leftCandleIndex < candles.size()) {
                current -= platesBeforeCandle[leftCandleIndex];
            } else {
                current -= plateCount;
            }

            if (rightCandleIndex >= 0) {
                current += platesBeforeCandle[rightCandleIndex];
            }

            result.push_back(std::max(current, 0));
        }

        return result;
    }
};

// @lc code=end

