/*
 * @lc app=leetcode id=1759 lang=cpp
 *
 * [1759] Count Number of Homogenous Substrings
 */

// @lc code=start
#include <string>
using std::string;
class Solution {
public:
    int countHomogenous(string s) 
    {
        const long MOD = 1000000007;
        int n = s.size();
        int l = 0;
        long result = 0;

        while (l < n)
        {
            int r = l + 1;
            while (r < n && s[l] == s[r])
            {
                r++;
            }

            result += (long)(r - l) * ((long)(r - l + 1)) / 2;
            result %= MOD;
            l = r;
        }

        return (int) result;
    }
};
// @lc code=end

