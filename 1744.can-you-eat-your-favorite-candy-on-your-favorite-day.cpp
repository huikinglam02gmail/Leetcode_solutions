/*
 * @lc app=leetcode id=1744 lang=cpp
 *
 * [1744] Can You Eat Your Favorite Candy on Your Favorite Day?
 */

// @lc code=start
#include <vector>;
using std::vector;
class Solution 
{
public:
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) 
    {
        vector<long> prefixSum = {0};
        for (auto it = candiesCount.begin(); it!= candiesCount.end(); ++it)
        {
            prefixSum.push_back(prefixSum.back() + *it);
        }

        vector<bool> result = {};
        for (auto &query : queries)
        {
            result.push_back(prefixSum[query.at(0)] / query.at(2) <= query.at(1) && query.at(1) < prefixSum[query.at(0) + 1]);
        }
        return result;
    }
};
// @lc code=end

