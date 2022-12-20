/*
 * @lc app=leetcode id=1552 lang=csharp
 *
 * [1552] Magnetic Force Between Two Balls
 */

// @lc code=start
public class Solution 
{
    int[] Position;

    public int ballCount(int d)
    {
        int curr = Position[0];
        int ans = 1;
        
        for (int i = 1; i < Position.Length; i++)
        {
            if (Position[i] - curr >= d)
            {
                curr = Position[i];
                ans++;
            }
        }
        return ans;
    }

    public int MaxDistance(int[] position, int m) 
    {
        Position = position;
        Array.Sort(Position);
        int l = 1;
        int r = Position[Position.Length-1] - Position[0];
        while (l < r)
        {
            int mid = r -((r - l) / 2);
            if (ballCount(mid) >= m)
            {
                l = mid;
            }
            else
            {
                r = mid - 1;
            }
        }
        return l;
    }
}
// @lc code=end

