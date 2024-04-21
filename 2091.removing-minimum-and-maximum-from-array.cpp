/*
 * @lc app=leetcode id=2091 lang=cpp
 *
 * [2091] Removing Minimum and Maximum From Array
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    /*
    Identify indices of max and min
    There are 3 possibilities:
    1. delete both from left
    2. delete min(minInd, maxInd) from left and max(minInd, maxInd) from right
    3. delete both from right
    */
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(3);
        int maxInd = -1, maxNum = INT_MIN, minInd = -1, minNum = INT_MAX;
        for (int i = 0; i < n; i++) {
            if (nums[i] > maxNum) {
                maxNum = nums[i];
                maxInd = i;
            }
            if (nums[i] < minNum) {
                minNum = nums[i];
                minInd = i;
            }
        }
        result[0] = max(maxInd, minInd) + 1;
        result[2] = n - min(maxInd, minInd);
        result[1] = min(minInd, maxInd) + 1 + n - max(minInd, maxInd);
        return min({result[0], result[1], result[2]});
    }
};

// @lc code=end

