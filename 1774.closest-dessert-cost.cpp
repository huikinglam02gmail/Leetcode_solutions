/*
 * @lc app=leetcode id=1774 lang=cpp
 *
 * [1774] Closest Dessert Cost
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::abs;
using std::vector;
class Solution {
private:
    vector<int> ToppingCosts;
    int Target;
    int result = -1;
    int resultDiff = INT_MAX;
    void Backtracking(int i, int diff) {
        if ((diff > 0 && abs(diff) < resultDiff) || (diff <= 0 && abs(diff) <= resultDiff)) {
            result = Target + diff;
            resultDiff = abs(diff);
        }

        if (diff < 0 && i < ToppingCosts.size()) {
            for (int j = 0; j < 3; j++) {
                Backtracking(i + 1, diff + j * ToppingCosts[i]);
            }
        }
    }

public:
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        Target = target;
        ToppingCosts = toppingCosts;

        for (int i = 0; i < baseCosts.size(); i++) {
            Backtracking(0, baseCosts[i] - target);
        }

        return result;
    }
};
// @lc code=end

