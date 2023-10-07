/*
 * @lc app=leetcode id=1014 lang=cpp
 *
 * [1014] Best Sightseeing Pair
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int n = values.size();
        int maxSoFar = 0;
        int last = 0;

        for (int i = 1; i < n; i++) {
            int current = values[i - 1] + values[i] - 1;

            if (i > 1) {
                current = max(current, last - values[i - 1] + values[i] - 1);
            }

            last = current;
            maxSoFar = max(maxSoFar, last);
        }

        return maxSoFar;
    }
};

// @lc code=end

