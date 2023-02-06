/*
 * @lc app=leetcode id=1637 lang=csharp
 *
 * [1637] Widest Vertical Area Between Two Points Containing No Points
 */

// @lc code=start
public class Solution 
{
    public int MaxWidthOfVerticalArea(int[][] points) 
    {
        SortedSet<int> xPos = new SortedSet<int>();
        foreach (int[] pos in points)
        {
            xPos.Add(pos[0]);
        }    

        int[] xList = xPos.ToArray();
        int result = 0;
        for (int i = 0; i < xList.Length - 1; i++)
        {
            result = Math.Max(result, xList[i + 1] - xList[i]);
        }
        return result;
    }
}
// @lc code=end

