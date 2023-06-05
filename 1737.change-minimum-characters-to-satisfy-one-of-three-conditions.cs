/*
 * @lc app=leetcode id=1737 lang=csharp
 *
 * [1737] Change Minimum Characters to Satisfy One of Three Conditions
 */

// @lc code=start
public class Solution
{
    public int MinCharacters(string a, string b)
    {
        int[] aCount = new int[26];
        int[] bCount = new int[26];
        foreach (char c in a)
        {
            aCount[c - 'a']++;
        }
        foreach (char c in b)
        {
            bCount[c - 'a']++;
        }

        int[] aPrefix = new int[27];
        int[] bPrefix = new int[27];
        for (int i = 0; i < 26; i++)
        {
            aPrefix[i + 1] = aPrefix[i] + aCount[i];
            bPrefix[i + 1] = bPrefix[i] + bCount[i];
        }

        int[] aAllBelow = new int[26];
        int[] bAllBelow = new int[26];
        aAllBelow[0] = aPrefix[26] - aPrefix[1];
        bAllBelow[0] = bPrefix[26] - bPrefix[1];
        for (int i = 1; i < 26; i++)
        {
            aAllBelow[i] = aAllBelow[i - 1] - aCount[i];
            bAllBelow[i] = bAllBelow[i - 1] - bCount[i];
        }

        int[] aAllAbove = new int[26];
        int[] bAllAbove = new int[26];
        aAllAbove[25] = aPrefix[25];
        bAllAbove[25] = bPrefix[25];
        for (int i = 24; i >= 0; i--)
        {
            aAllAbove[i] = aAllAbove[i + 1] - aCount[i];
            bAllAbove[i] = bAllAbove[i + 1] - bCount[i];
        }

        int[] aAllThis = new int[26];
        int[] bAllThis = new int[26];
        for (int i = 0; i < 26; i++)
        {
            aAllThis[i] = aPrefix[26] - aPrefix[i + 1] + aPrefix[i];
            bAllThis[i] = bPrefix[26] - bPrefix[i + 1] + bPrefix[i];
        }

        int result = int.MaxValue;
        for (int i = 0; i < 25; i++)
        {
            result = Math.Min(result, aAllBelow[i] + bAllAbove[i + 1]);
        }
        for (int i = 0; i < 25; i++)
        {
            result = Math.Min(result, bAllBelow[i] + aAllAbove[i + 1]);
        }
        for (int i = 0; i < 26; i++)
        {
            for (int j = 0; j < 26; j++)
            {
                result = Math.Min(result, aAllThis[i] + bAllThis[j]);
            }
        }
        return result;
    }
}

// @lc code=end

