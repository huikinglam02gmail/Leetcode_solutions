/*
 * @lc app=leetcode id=1750 lang=cpp
 *
 * [1750] Minimum Length of String After Deleting Similar Ends
 */

// @lc code=start
#include <string>;
using std::string;
class Solution 
{
public:
    int minimumLength(string s) 
    {
        int n = s.size();
        int i = 0;
        int j = n - 1;
        while (i < j && s[i] == s[j])
        {
            char common = s[i];
            while (i < n && s[i] == common && i <= j)
            {
                i++;
            }
            while (j >= 0 && s[j] == common && i <= j)
            {
                j--;
            }
        }
        return j - i + 1;       
    }
};
// @lc code=end

