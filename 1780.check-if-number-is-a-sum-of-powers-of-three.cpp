/*
 * @lc app=leetcode id=1780 lang=cpp
 *
 * [1780] Check if Number is a Sum of Powers of Three
 */

// @lc code=start
#include<vector>
using std::vector;
class Solution {
private:
    int setBitNumber(int n)
    {
        if (n == 0)
            return 0;
    
        int msb = 0;
        n = n / 2;
        while (n != 0) {
            n = n / 2;
            msb++;
        }
    
        return (1 << msb);
    }
public:
    bool checkPowersOfThree(int n) {
        int thres = 0;
        int temp = 1;
        while (temp <= n)
        {
            thres++;
            temp *= 3;
        }

        vector<int> dp = vector<int> (1 << thres, 0);
        temp = 1;
        for (int j = 0; j < thres; j++)
        {
            dp[1 << j] = temp;
            temp *= 3;
        }

        for (int mask = 1; mask < (1 << thres); mask++)
        {
            dp[mask] = dp[setBitNumber(mask)] + dp[mask - setBitNumber(mask)];         
        }

        return find(dp.begin(), dp.end(),n) != dp.end();
    }
};
// @lc code=end

