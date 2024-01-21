/*
 * @lc app=leetcode id=2566 lang=csharp
 *
 * [2566] Maximum Difference by Remapping a Digit
 */

// @lc code=start
public class Solution
{
    /**
     * There are only 10 digits. In terms of a map, there are 100 keys.
     * Use the 100 keys and record max and min of the result and take the difference.
     */
    public int MinMaxDifference(int num)
    {
        List<int> master = num.ToString().Select(c => int.Parse(c.ToString())).ToList();
        long minResult = long.MaxValue;
        long maxResult = long.MinValue;

        for (int i = 0; i < 10; i++)
        {
            if (master.Contains(i))
            {
                for (int j = 0; j < 10; j++)
                {
                    long modified = 0;

                    for (int k = 0; k < master.Count; k++)
                    {
                        if (master[k] == i)
                            modified += j;
                        else
                            modified += master[k];

                        modified *= 10;
                    }

                    minResult = Math.Min(minResult, modified / 10);
                    maxResult = Math.Max(maxResult, modified / 10);
                }
            }
        }

        return Convert.ToInt32(maxResult - minResult);
    }
}

// @lc code=end

