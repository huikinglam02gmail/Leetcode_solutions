/*
 * @lc app=leetcode id=2023 lang=cpp
 *
 * [2023] Number of Pairs of Strings With Concatenation Equal to Target
 */

// @lc code=start
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
        int n = target.length();
        unordered_map<string, int> hashTable;

        for (int i = 0; i < n - 1; i++) {
            string prefix = target.substr(0, i + 1);
            if (hashTable.find(prefix) == hashTable.end()) {
                hashTable[prefix] = 0;
            }

            string suffix = target.substr(i + 1);
            if (hashTable.find(suffix) == hashTable.end()) {
                hashTable[suffix] = 0;
            }
        }

        for (const string& num : nums) {
            if (hashTable.find(num) != hashTable.end()) {
                hashTable[num]++;
            }
        }

        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            string prefix = target.substr(0, i + 1);
            string suffix = target.substr(i + 1);

            if (prefix == suffix) {
                result += hashTable[prefix] * (hashTable[prefix] - 1);
            } else {
                result += hashTable[prefix] * hashTable[suffix];
            }
        }

        return result;
    }
};

// @lc code=end

