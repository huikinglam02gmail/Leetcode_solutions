/*
 * @lc app=leetcode id=744 lang=cpp
 *
 * [744] Find Smallest Letter Greater Than Target
 */

// @lc code=start
#include <vector>;
using std::upper_bound;
using std::vector;
class Solution 
{
public:
    char nextGreatestLetter(vector<char>& letters, char target) 
    {
        return letters.at((upper_bound(letters.begin(), letters.end(), target) - letters.begin()) % letters.size());
    }
};
// @lc code=end

