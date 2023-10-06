/*
 * @lc app=leetcode id=1931 lang=cpp
 *
 * [1931] Painting a Grid With Three Different Colors
 */

// @lc code=start
#include <vector>
#include <deque>
#include <unordered_map>
#include <cmath>
#include <unordered_set>

class Solution {
public:
    bool statesAreCompatible(int state1, int state2) {
        while (state1 > 0 && state2 > 0) {
            if (state1 % (1 << 3) == state2 % (1 << 3)) {
                return false;
            }
            state1 >>= 3;
            state2 >>= 3;
        }
        return true;
    }

    int colorTheGrid(int m, int n) {
        const int MOD = pow(10, 9) + 7;
        std::deque<int> dq;
        int steps = 0;
        dq.push_back(0);

        while (!dq.empty() && steps < m) {
            int dqSize = dq.size();
            for (int i = 0; i < dqSize; i++) {
                int state = dq.front();
                dq.pop_front();
                int newState = state << 3;
                for (int j = 0; j < 3; j++) {
                    if ((state % (1 << 3)) != (1 << j)) {
                        dq.push_back(newState ^ (1 << j));
                    }
                }
            }
            steps++;
        }

        if (n == 1) {
            return dq.size();
        }

        std::vector<int> possibleStates(dq.begin(), dq.end());

        std::unordered_map<int, std::unordered_set<int>> currentToPrevMap;
        for (int key : possibleStates) {
            currentToPrevMap[key] = std::unordered_set<int>();
            for (int key1 : possibleStates) {
                if (statesAreCompatible(key, key1)) {
                    currentToPrevMap[key].insert(key1);
                }
            }
        }

        std::unordered_map<int, int> dp;
        for (int key : possibleStates) {
            dp[key] = 1;
        }

        for (int j = 1; j < n; j++) {
            std::unordered_map<int, int> dpNew;
            for (auto item : currentToPrevMap) {
                dpNew[item.first] = 0;
                for (int oldKey : item.second) {
                    dpNew[item.first] = (dpNew[item.first] + dp[oldKey]) % MOD;
                }
            }
            dp = dpNew;
        }

        int result = 0;
        for (auto item : dp) {
            result = (result + dp[item.first]) % MOD;
        }
        return result;
    }
};

// @lc code=end

