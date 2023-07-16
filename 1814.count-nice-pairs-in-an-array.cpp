/*
 * @lc app=leetcode id=1814 lang=cpp
 *
 * [1814] Count Nice Pairs in an Array
 */

// @lc code=start
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::unordered_map;
using std::unordered_set;
using std::vector;

class Solution {
public:
    /*
     * First prepare the second array rev(nums)
     * Then given the condition nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
     * nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
     * So we just maintain this difference and maintain a set
     */
    int countNicePairs(vector<int>& nums) {
        unordered_map<int, unordered_set<int>> hashTable;
        long long result = 0;
        long long MOD = 1000000007;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int diff = num - reverseNumber(num);
            if (hashTable.find(diff) == hashTable.end()) {
                hashTable[diff] = unordered_set<int>();
            }
            hashTable[diff].insert(i);
        }

        for (const auto& v : hashTable) {
            long long count = static_cast<long long>(v.second.size());
            result += count * (count - 1) / 2;
            result %= MOD;
        }

        return static_cast<int>(result);
    }

private:
    int reverseNumber(int num) {
        int reversed = 0;
        while (num > 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }
        return reversed;
    }
};

// @lc code=end

