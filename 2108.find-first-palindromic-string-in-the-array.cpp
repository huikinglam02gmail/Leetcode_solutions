/*
 * @lc app=leetcode id=2108 lang=cpp
 *
 * [2108] Find First Palindromic String in the Array
 */

// @lc code=start
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for (const string& word : words) {
            int i = 0, j = word.length() - 1;
            while (i < j && word[i] == word[j]) {
                i++;
                j--;
            }
            if (i >= j) {
                return word;
            }
        }
        return "";
    }
};
// @lc code=end

