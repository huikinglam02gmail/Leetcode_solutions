/*
 * @lc app=leetcode id=2839 lang=cpp
 *
 * [2839] Check if Strings Can be Made Equal With Operations I
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
    bool canBeEqual(string s1, string s2) {
        if (s1 == s2) return true;
        
        string reversed1 = string(1, s1[2]) + s1[1] + s1[0] + s1[3];
        string reversed2 = string(1, s1[2]) + s1[3] + s1[0] + s1[1];
        string reversed3 = string(1, s1[0]) + s1[3] + s1[2] + s1[1];
        
        if (reversed1 == s2 || reversed2 == s2 || reversed3 == s2) return true;
        
        return false;
    }
};


// @lc code=end

