/*
 * @lc app=leetcode id=2937 lang=csharp
 *
 * [2937] Make Three Strings Equal
 */

// @lc code=start
public class Solution {
    public int FindMinimumOperations(string s1, string s2, string s3) {
        string[] lengthOrder = new string[] { s1, s2, s3 };
        Array.Sort(lengthOrder, (x, y) => x.Length.CompareTo(y.Length));
        int i = lengthOrder[0].Length;
        while (i > 0 && (!lengthOrder[1].StartsWith(lengthOrder[0].Substring(0, i)) || !lengthOrder[2].StartsWith(lengthOrder[0].Substring(0, i)))) {
            i--;
        }
        if (i == 0) {
            return -1;
        }
        else {
            return lengthOrder.Sum(x => x.Length - i);
        }
    }
}

// @lc code=end

