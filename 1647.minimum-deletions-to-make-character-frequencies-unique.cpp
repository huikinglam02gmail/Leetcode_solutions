/*
 * @lc app=leetcode id=1647 lang=cpp
 *
 * [1647] Minimum Deletions to Make Character Frequencies Unique
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDeletions(string s) {
        vector<int> hashTable(26, 0);
        for (char c : s) {
            hashTable[c - 'a']++;
        }
        
        sort(hashTable.rbegin(), hashTable.rend());
        int result = 0;
        int maxFreq = hashTable[0];
        
        for (int count : hashTable) {
            if (count >= maxFreq) {
                result += count - maxFreq;
            } else {
                maxFreq = count;
            }
            
            if (maxFreq > 0) {
                maxFreq--;
            }
        }
        
        return result;
    }
};

// @lc code=end

