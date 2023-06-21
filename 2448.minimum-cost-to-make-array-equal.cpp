/*
 * @lc app=leetcode id=2448 lang=cpp
 *
 * [2448] Minimum Cost to Make Array Equal
 */

// @lc code=start
#include<vector>
#include<algorithm>
#include<iostream>
using std::make_tuple;
using std::sort;
using std::vector;
using std::min;
class Solution {
private:
    bool static sort2D( const vector<int>& v1,
               const vector<int>& v2 ) {
    return v1[0] != v2[0] ? v1[0] < v2[0] : v1[1] < v2[1];
}
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int n = nums.size();
        vector<vector<int>> data {};
        for (int i = 0; i < n; i++)
        {
            vector<int> datum{nums[i], cost[i]};
            data.push_back(datum);
        }
        sort(data.begin(), data.end(), sort2D);
        vector<long long> prefix_cost {(long long)0};
        vector<long long> prefix_mult {(long long)0};
        for (vector<int> item : data)
        {
            prefix_cost.push_back(prefix_cost.back() + (long long)item[1]);
            prefix_mult.push_back(prefix_mult.back() + (long long)item[0] * (long long)item[1]);
        }
        long long result = INT64_MAX;
        for (int i = 0; i < n; i++)
        {
            result = min(result, prefix_mult.back() - prefix_mult[i+1] - prefix_mult[i] + (data[i][0])*(prefix_cost[i+1] + prefix_cost[i] - prefix_cost.back()));
        }
        return result;
    }
};
// @lc code=end

