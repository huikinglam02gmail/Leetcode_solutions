/*
 * @lc app=leetcode id=1910 lang=cpp
 *
 * [1910] Remove All Occurrences of a Substring
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
    string removeOccurrences(string s, string part) {
        string result;
        int n = part.size();
        
        for (char c : s) {
            result.push_back(c);
            
            if (result.size() >= n && result.substr(result.size() - n) == part) {
                for (int j = 0; j < n; j++) {
                    result.pop_back();
                }
            }
        }
        
        return result;
    }
};

// @lc code=end

