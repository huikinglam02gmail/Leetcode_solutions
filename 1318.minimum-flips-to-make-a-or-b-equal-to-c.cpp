/*
 * @lc app=leetcode id=1318 lang=cpp
 *
 * [1318] Minimum Flips to Make a OR b Equal to c
 */

// @lc code=start
#include <algorithm>;
class Solution 
{
public:
    int minFlips(int a, int b, int c) 
    {
        int result = 0;
        for (int i = 0; i < 32; i++) 
        {
            if ((c & (1 << i)) == 0) 
            {
                result += int((a & (1 << i)) != 0) + int((b & (1 << i)) != 0);
            }
            else 
            {
                result += std::max(1, int((a & (1 << i)) == 0) + int((b & (1 << i)) == 0)) - 1;
            }
        }
        return result;    
    }
};
// @lc code=end

