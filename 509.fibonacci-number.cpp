/*
 * @lc app=leetcode id=509 lang=cpp
 *
 * [509] Fibonacci Number
 */

// @lc code=start
class Solution 
{
    public:
        int fib(int n) 
        {
            if (n <= 1)
            {
                return n;
            }
            else
            {
                int o1 = 0;
                int o2 = 1;
                int nw = o1 + o2;
                int temp;
                for (int i = 0; i < n - 2; ++i)
                {
                    o1 = o2;
                    temp = o2;
                    o2 = nw;
                    nw += temp;
                }
                return nw;
            }
        }
};
// @lc code=end

