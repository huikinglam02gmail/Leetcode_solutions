/*
 * @lc app=leetcode id=2958 lang=cpp
 *
 * [2958] Length of Longest Subarray With at Most K Frequency
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int, int> hashTable;
        int left = 0;
        int result = 0;
        for (int right = 0; right < nums.size(); right++) {
            int num = nums[right];
            while (hashTable.count(num) && hashTable[num] == k) {
                if (hashTable.count(nums[left])) {
                    hashTable[nums[left]]--;
                    if (hashTable[nums[left]] == 0) {
                        hashTable.erase(nums[left]);
                    }
                }
                left++;
            }
            hashTable[num] = hashTable[num] + 1;
            result = max(result, right - left + 1);
        }
        return result;
    }
};

// @lc code=end

