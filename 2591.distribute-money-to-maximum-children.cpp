/*
 * @lc app=leetcode id=2591 lang=cpp
 *
 * [2591] Distribute Money to Maximum Children
 */

// @lc code=start
#include <map>
#include <tuple>
#include <algorithm>

class Solution {
private:
    std::map<std::tuple<int, int>, int> memo;

public:
    /**
     * Follow the rule
     */
    int distMoney(int money, int children) {
        if (money < children) {
            return -1;
        }

        if (children == 1) {
            if (money == 4) {
                return -1;
            } else if (money == 8) {
                return 1;
            } else {
                return 0;
            }
        }

        auto key = std::make_tuple(money, children);

        auto it = memo.find(key);
        if (it != memo.end()) {
            return it->second;
        }

        int result = 0;

        for (int i = 1; i < std::min(money, 9); i++) {
            if (i == 4) {
                continue;
            }

            int nextStep = distMoney(money - i, children - 1);

            if (nextStep >= 0) {
                result = std::max(result, (i == 8) ? 1 + nextStep : 0);
            }
        }

        memo[key] = result;
        return result;
    }
};

// @lc code=end

