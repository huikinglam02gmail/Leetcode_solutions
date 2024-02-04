/*
 * @lc app=leetcode id=2744 lang=cpp
 *
 * [2744] Find Maximum Number of String Pairs
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int maximumNumberOfStringPairs(std::vector<std::string>& words) {
        int result = 0;
        std::unordered_map<std::string, int> hashTable;

        for (const std::string& word : words) {
            if (hashTable.find(word) != hashTable.end()) {
                result += hashTable[word];
            }
            std::string reversedWord = word;
            std::reverse(reversedWord.begin(), reversedWord.end());
            hashTable[reversedWord] = hashTable.count(reversedWord) ? hashTable[reversedWord] + 1 : 1;
        }

        return result;
    }
};

// @lc code=end

