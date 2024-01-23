/*
 * @lc app=leetcode id=2578 lang=csharp
 *
 * [2578] Split With Minimum Sum
 */

// @lc code=start
using System;
using System.Linq;

public class Solution
{
    /**
     * Sort the digits, add up odd and even digits
     */
    public int SplitNum(int num)
    {
        int[] arr = num.ToString().Select(c => int.Parse(c.ToString())).ToArray();
        Array.Sort(arr);

        string[] newArr = { "", "" };
        for (int i = 0; i < arr.Length; i++)
        {
            newArr[i % 2] += arr[i].ToString();
        }

        return int.Parse(newArr[0]) + int.Parse(newArr[1]);
    }
}

// @lc code=end

