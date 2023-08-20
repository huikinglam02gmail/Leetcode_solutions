/*
 * @lc app=leetcode id=1862 lang=cpp
 *
 * [1862] Sum of Floored Pairs
 */

// @lc code=start
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int sumOfFlooredPairs(vector<int>& nums) {
        unordered_map<int, int> hashTable;
        
        for (int num : nums) {
            if (hashTable.count(num)) {
                hashTable[num]++;
            } else {
                hashTable[num] = 1;
            }
        }
        
        int maxKey = 0;
        for (const auto& kvp : hashTable) {
            maxKey = max(maxKey, kvp.first);
        }
        
        vector<int> increment(maxKey, 0);
        
        for (const auto& kvp : hashTable) {
            int key = kvp.first;
            for (int j = key; j <= increment.size(); j += key) {
                increment[j - 1] += kvp.second;
            }
        }
        
        vector<long long> prefixSum = { (long long)0 };
        
        for (int inc : increment) {
            prefixSum.push_back(prefixSum.back() + (long long)inc);
        }
        
        long long result = 0;
        long long MOD = 1000000007;
        
        for (const auto& kvp : hashTable) {
            int key = kvp.first;
            result += static_cast<long long>(kvp.second) * prefixSum[key];
            result %= MOD;
        }
        
        return static_cast<int>(result);
    }
};

// @lc code=end

