/*
 * @lc app=leetcode id=389 lang=cpp
 *
 * [389] Find the Difference
 */

// @lc code=start
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    char findTheDifference(string s, string t) {
        vector<int> sCount(26, 0);
        vector<int> tCount(26, 0);
        
        for (char c : s) {
            sCount[c - 'a']++;
        }
        
        for (char c : t) {
            tCount[c - 'a']++;
        }
        
        for (int i = 0; i < 26; i++) {
            if (sCount[i] != tCount[i]) {
                return static_cast<char>('a' + i);
            }
        }
        
        return ' ';
    }
};

// @lc code=end

