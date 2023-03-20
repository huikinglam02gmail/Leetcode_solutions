/*
 * @lc app=leetcode id=1686 lang=csharp
 *
 * [1686] Stone Game VI
 */

// @lc code=start
using System.Linq;
public class Solution 
{
    public int StoneGameVI(int[] aliceValues, int[] bobValues) 
    {
        int[][] data = aliceValues.Zip(bobValues, (first, second) => new int[2]{first, second}).OrderBy(x => - x[0] - x[1]).ToArray();

        int alice = 0;
        int bob = 0;
        for (int i = 0; i < data.Length; i++)
        {
            if (i % 2 == 0)
            {
                alice += data[i][0];
            }
            else
            {
                bob += data[i][1];
            }
        }

        if (alice > bob)
        {
            return 1;
        }
        else if (alice == bob)
        {
            return 0;
        }
        else
        {
            return -1;
        }
    }
}
// @lc code=end

