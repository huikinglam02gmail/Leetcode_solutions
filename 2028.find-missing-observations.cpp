/*
 * @lc app=leetcode id=2028 lang=cpp
 *
 * [2028] Find Missing Observations
 */

// @lc code=start
#include <vector>
#include <numeric>  // for std::accumulate

class Solution {
public:
    std::vector<int> missingRolls(std::vector<int>& rolls, int mean, int n) {
        int sumAns = mean * (rolls.size() + n) - std::accumulate(rolls.begin(), rolls.end(), 0);
        std::vector<int> result;

        if (n <= sumAns && sumAns <= 6 * n) {
            int defaultDice = sumAns / n;
            result.assign(n, 0);

            for (int i = 0; i < n; i++) {
                result[i] += defaultDice;
                sumAns -= defaultDice;
            }

            int ind = 0;
            while (sumAns > 0) {
                result[ind] += 1;
                sumAns -= 1;
                ind += 1;
            }
        }

        return result;
    }
};

// @lc code=end

