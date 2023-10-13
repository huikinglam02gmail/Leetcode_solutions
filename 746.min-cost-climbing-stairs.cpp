/*
 * @lc app=leetcode id=746 lang=cpp
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
/**
 * @lc app=leetcode id=746 lang=cpp
 *
 * [746] Min Cost Climbing Stairs
 */

#include <vector>
using namespace std;

class Solution {
public:
    /*
    DP question clearly
    dp[i] = min cost to reach i
    0 and 1 are trivial    
    */
    int minCostClimbingStairs(vector<int>& cost) {
        int a = 0, b = 0;
        int n = cost.size();

        for (int i = 0; i < n; i++) {
            int temp = a;
            a = b;
            b = min(temp, b) + cost[i];
        }

        return min(a, b);
    }
};

// @lc code=end

