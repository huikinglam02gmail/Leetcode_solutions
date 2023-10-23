/*
 * @lc app=leetcode id=342 lang=cpp
 *
 * [342] Power of Four
 */

// @lc code=start
#include <string>
#include <bitset>
using std::bitset;
using std::count;
using std::reverse;
using std::string;
class Solution 
{
public:
    bool isPowerOfFour(int n) 
    {
        if (n > 0) 
        {
            string nBinary = bitset<32>(n).to_string();
            reverse(nBinary.begin(), nBinary.end());

            if (count(nBinary.begin(), nBinary.end(), '1') == 1 && nBinary.find('1') % 2 == 0) 
            {
                return true;
            }
        }
        return false;
    }
};

// @lc code=end

