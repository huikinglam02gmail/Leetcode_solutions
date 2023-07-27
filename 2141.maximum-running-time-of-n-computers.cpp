/*
 * @lc app=leetcode id=2141 lang=cpp
 *
 * [2141] Maximum Running Time of N Computers
 */

// @lc code=start
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        sort(batteries.begin(), batteries.end());
        long long S = 0;
        for (int battery : batteries) {
            S += (long long)battery;
        }
        int j = batteries.size() - 1;
        while ((long long)batteries[j] > S / n) {
            n--;
            S -= (long long)batteries[j];
            j--;
        }
        return S / (long long)n;
    }
};

// @lc code=end

