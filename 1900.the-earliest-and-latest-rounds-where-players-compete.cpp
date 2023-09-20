/*
 * @lc app=leetcode id=1900 lang=cpp
 *
 * [1900] The Earliest and Latest Rounds Where Players Compete
 */

// @lc code=start
#include <vector>
#include <map>
#include <tuple>
#include <algorithm>

class Solution {
private:
    int n;
    int firstPlayer;
    int secondPlayer;
    std::map<std::tuple<int, int, int>, std::vector<int>> memo;

public:
    std::vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        this->n = n;
        this->firstPlayer = firstPlayer;
        this->secondPlayer = secondPlayer;

        return DP((1 << n) - 1, 0, 1);
    }

private:
    std::vector<int> DP(int competitors, int winners, int round) {
        std::tuple<int, int, int> t = std::make_tuple(competitors, winners, round);

        if (memo.find(t) == memo.end()) 
        {
            std::vector<int> result(2, INT_MAX);

            if (competitors == 0) {
                result = DP(winners, 0, round + 1);
            } else {
                int l = 0, r = n - 1;

                while (l < n && ((competitors & (1 << l)) == 0)) {
                    l++;
                }

                while (r >= 0 && ((competitors & (1 << r)) == 0)) {
                    r--;
                }

                competitors ^= (1 << l);

                if (l < r) {
                    competitors ^= (1 << r);
                }

                if (l == firstPlayer - 1 && r == secondPlayer - 1) {
                    result = { round, round };
                } else if (l == firstPlayer - 1 || l == secondPlayer - 1) {
                    result = DP(competitors, winners ^ (1 << l), round);
                } else if (r == firstPlayer - 1 || r == secondPlayer - 1) {
                    result = DP(competitors, winners ^ (1 << r), round);
                } else {
                    std::vector<int> leftWins = DP(competitors, winners ^ (1 << l), round);
                    std::vector<int> rightWins = DP(competitors, winners ^ (1 << r), round);
                    result[0] = std::min(leftWins[0], rightWins[0]);
                    result[1] = std::max(leftWins[1], rightWins[1]);
                }
            }

            memo[t] = result;
        }
        return memo[t];
    }
};

// @lc code=end

