/*
 * @lc app=leetcode id=1569 lang=cpp
 *
 * [1569] Number of Ways to Reorder Array to Get Same BST
 */

// @lc code=start
#include <vector>
using std::vector;
class Solution 
{
private:
    vector<vector<long long>> nCr;
    vector<long long> row;
    const long long MOD = 1000000007;
public:
    void initiatenCr(int n)
    {
        nCr.push_back({1});
        nCr.push_back({1, 2, 1});
        for (int i = 2; i < n; i++)
        {
            row = { 1 };
            for (int j = 0; j < nCr.back().size() - 1; j++)
            {
                row.push_back((nCr.back()[j] + nCr.back()[j + 1]) % MOD);
            }
            row.push_back(1);
            nCr.push_back(row);
        }
    }

    long divideAndConquer(vector<int>& arr)
    {
        int n = arr.size(); 
        if (n < 3)
        {
            return (long)1;
        }
        int root = arr[0];
        vector<int> left {};
        vector<int> right {};
        for (int i : arr)
        {
            if (i < root)
            {
                left.push_back(i);
            }
            else if (i > root)
            {
                right.push_back(i);
            }
        }
        int nl = left.size();
        return (((nCr[n - 2][nl] % MOD) * divideAndConquer(left)) % MOD * (divideAndConquer(right))) % MOD; 
    }

    int numOfWays(vector<int>& nums) 
    {
        initiatenCr(nums.size());
        return (int)(divideAndConquer(nums) - 1);
    }
};
// @lc code=end

