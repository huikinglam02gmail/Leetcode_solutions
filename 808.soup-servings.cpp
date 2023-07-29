/*
 * @lc app=leetcode id=808 lang=cpp
 *
 * [808] Soup Servings
 */

// @lc code=start
#include <iostream>
#include <map>
#include <tuple>
#include <cmath>
using std::make_tuple;
using std::map;
using std::pow;
using std::tuple;

class Solution {
public:
    /*
     * Operation 1: A -= 100
     * Operation 2: A -= 75, B -= 25
     * Operation 3: A -= 50, B -= 50
     * Operation 4: A -= 25, B -= 75
     * Maintain status of A and B and round.
     * Since after each round, the modification will add 1/(4^k) to the probability.
     * We can see that when n becomes large, the answer goes towards 1.
     * To find out the exact limit I manually binary search on the n threshold and found it to be 4801.
     */
    map<tuple<int, int, int>, double> memo;

    double Dfs(int A, int B, int k) {
        if (A <= 0 && B > 0)
            return 1 / pow(4, k);
        if (A <= 0 && B <= 0)
            return 1 / (2 * pow(4, k));
        if (A > 0 && B <= 0)
            return 0;
        tuple<int, int, int> t = make_tuple(A, B, k);
        if (memo.find(t) == memo.end()) {
            double result = 0;
            result += Dfs(A - 100, B, k + 1);
            result += Dfs(A - 75, B - 25, k + 1);
            result += Dfs(A - 50, B - 50, k + 1);
            result += Dfs(A - 25, B - 75, k + 1);
            memo[t] = result;
        }
        return memo[t];
    }

    double soupServings(int n) {
        memo.clear();
        return n > 4800 ? 1 : Dfs(n, n, 0);
    }
};

// @lc code=end

