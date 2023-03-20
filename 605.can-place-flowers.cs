/*
 * @lc app=leetcode id=605 lang=csharp
 *
 * [605] Can Place Flowers
 */

// @lc code=start
public class Solution 
{
    public bool CanPlaceFlowers(int[] flowerbed, int n) 
    {
        int consec = 1;
        int free = 0;
        for (int i = 0; i < flowerbed.Length; i++)
        {
            if (flowerbed[i] == 0)
            {
                consec++;
            }
            else
            {
                if (consec > 0)
                {
                    free += (consec - 1)/2;
                }
                consec = 0;
            }
        }
        if (consec > 0)
        {
            free += consec / 2;
        }
        return free >= n;
    }
}
// @lc code=end

