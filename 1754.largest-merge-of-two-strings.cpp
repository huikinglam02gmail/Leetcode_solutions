/*
 * @lc app=leetcode id=1754 lang=cpp
 *
 * [1754] Largest Merge Of Two Strings
 */

// @lc code=start
#include <string>
using std::string;
class Solution {
public:
    string largestMerge(string word1, string word2) {
        int i = 0;
        int j = 0;
        int n1 = word1.size();
        int n2 = word2.size();
        if (n1 == 0)
        {
            return word2;
        }
        else if (n2 == 0)
        {
            return word1;
        }
        else
        {
            if (word1 >= word2)
            {
                return word1[0] + largestMerge(word1.substr(1), word2);
            }
            else
            {
                return word2[0] + largestMerge(word1, word2.substr(1));
            }
        }
    }
};
// @lc code=end

