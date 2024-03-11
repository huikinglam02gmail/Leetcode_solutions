/*
 * @lc app=leetcode id=791 lang=cpp
 *
 * [791] Custom Sort String
 */

// @lc code=start
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> hashTable;
        string rest = "";
        
        for (char c : s) {
            if (order.find(c) != string::npos) {
                if (hashTable.find(c) == hashTable.end()) {
                    hashTable[c] = 0;
                }
                hashTable[c]++;
            } else {
                rest += c;
            }
        }
        
        string result = "";
        for (char c : order) {
            if (hashTable.find(c) != hashTable.end()) {
                for (int j = 0; j < hashTable[c]; j++) {
                    result += c;
                }
            }
        }
        
        result += rest;
        return result;
    }
};

// @lc code=end

