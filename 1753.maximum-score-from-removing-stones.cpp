/*
 * @lc app=leetcode id=1753 lang=cpp
 *
 * [1753] Maximum Score From Removing Stones
 */

// @lc code=start
#include <queue>
using std::priority_queue;
class Solution 
{
public:
    int maximumScore(int a, int b, int c) 
    {
        priority_queue<int> heap;
        heap.push(a);
        heap.push(b);
        heap.push(c);
        int result = 0;
        
        while (heap.size() >= 2) 
        {
            int x = heap.top();
            heap.pop();
            int y = heap.top();
            heap.pop();

            if (heap.size() > 0) 
            {
                int z = heap.top();
                result += y - z + 1;
                x -= (y - z + 1);
                y = z - 1;
                
                if (y > 0) 
                {
                    heap.push(y);
                }
                
                if (x > 0) 
                {
                    heap.push(x);
                }
            } 
            else 
            {
                result += y;
            }
        }       
        return result;            
    }
};
// @lc code=end

