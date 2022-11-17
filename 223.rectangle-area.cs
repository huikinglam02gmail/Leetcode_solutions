/*
 * @lc app=leetcode id=223 lang=csharp
 *
 * [223] Rectangle Area
 */

// @lc code=start
public class Solution 
{
    public int ComputeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) 
    {
        if (ax1 > bx1)
        {
            int temp = ax1;
            ax1 = bx1;
            bx1 = temp;
            temp = ay1;
            ay1 = by1;
            by1 = temp;
            temp = ax2;
            ax2 = bx2;
            bx2 = temp;
            temp = ay2;
            ay2 = by2;
            by2 = temp;
        }
        int result = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1);
        if ((by2 >= ay1 && ax2 >= bx1 && by1 <= ay1) || (ay2 >= by1 && ax2 >= bx1 && by2 >= ay2))
        {
            result -= (Math.Min(ay2,by2) - Math.Max(ay1,by1))*(Math.Min(ax2,bx2) - Math.Max(ax1,bx1));   
        }
        else if (by1 >= ay1 && by2 <= ay2 && ax2 >= bx1)
        {
            result -= (by2-by1)*(Math.Min(bx2,ax2)-bx1);
        }
        return result;
    }
}
// @lc code=end

