/*
 * @lc app=leetcode id=1787 lang=cpp
 *
 * [1787] Make the XOR of All Segments Equal to Zero
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<algorithm>
using std::max;
using std::min;
using std::move;
using std::pair;
using std::unordered_map;
using std::vector;

class Solution
{
public:
    int minChanges(vector<int>& nums, int k)
    {
        vector<unordered_map<int, int>> occur(k, unordered_map<int, int>{});
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            int key = i % k;
            if (occur[key].find(nums[i]) == occur[key].end())
            {
                occur[key].insert({nums[i], 0});
            }
            occur[key][nums[i]]++;
        }

        unordered_map<int, int> dp = occur[0];
        unordered_map<int, int> dpNew{};
        for (int i = 1; i < k; i++)
        {
            for (auto it = occur[i].begin(); it != occur[i].end(); it++)
            {
                for (auto it1 = dp.begin(); it1 != dp.end(); it1++)
                {
                    int key1 = it->first;
                    int key2 = it1->first;
                    if (dpNew.find(key1 ^ key2) == dpNew.end())
                    {
                        dpNew.insert({key1 ^ key2, 0});
                    }
                    dpNew[key1 ^ key2] = max(dpNew[key1 ^ key2], (it->second) + (it1->second));                    
                }
            }
            dp = move(dpNew);
        }

        int maxOccur = dp.find(0) != dp.end() ? dp[0] : 0;
        int minOccurSum = INT_MAX;
        int maxOccurSum = 0;

        for (int i = 0; i < k; i++)
        {
            int toAttach = 0;
            for (auto it = occur[i].begin(); it != occur[i].end(); it++)
            {
                toAttach = max(toAttach, it->second);
            }
            minOccurSum = min(minOccurSum, toAttach);
            maxOccurSum += toAttach;
        }
        return n - max(maxOccur, maxOccurSum - minOccurSum);        
    }
};
// @lc code=end

