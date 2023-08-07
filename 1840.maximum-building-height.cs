/*
 * @lc app=leetcode id=1840 lang=csharp
 *
 * [1840] Maximum Building Height
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int MaxBuilding(int n, int[][] restrictions)
    {
        List<int[]> restrictionsList = new List<int[]>(restrictions);
        restrictionsList.Add(new int[] { 1, 0 });
        restrictionsList.Sort((a, b) => a[0].CompareTo(b[0]));

        if (restrictionsList[^1][0] != n)
        {
            restrictionsList.Add(new int[] { n, n - 1 });
        }

        int resultLeftToRight = Scan(restrictionsList);
        restrictionsList.Reverse();
        int resultRightToLeft = Scan(restrictionsList);

        return Math.Min(resultLeftToRight, resultRightToLeft);
    }

    private int Scan(List<int[]> restrictions)
    {
        int n = restrictions.Count;
        int result = 0;

        for (int i = 0; i < n - 1; i++)
        {
            int h = restrictions[i][1] + Math.Abs(restrictions[i + 1][0] - restrictions[i][0]);

            if (h > restrictions[i + 1][1])
            {
                h = restrictions[i + 1][1] + (h - restrictions[i + 1][1]) / 2;
            }

            result = Math.Max(result, h);
            restrictions[i + 1][1] = Math.Min(restrictions[i + 1][1], h);
        }

        return result;
    }
}

// @lc code=end

