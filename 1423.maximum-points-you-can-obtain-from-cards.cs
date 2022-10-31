/*
 * @lc app=leetcode id=1423 lang=csharp
 *
 * [1423] Maximum Points You Can Obtain from Cards
 */

// @lc code=start
public class Solution {
    public int MaxScore(int[] cardPoints, int k) {
        int n = cardPoints.Length;
        int result = 0;
        List<int> prefix = new List<int>{0};
        foreach (int point in cardPoints)
        {
            prefix.Add(prefix[prefix.Count-1]+point);
        }
        for (int i = n-k; i < n+1; i++)
        {
            result = Math.Max(prefix[prefix.Count-1]-prefix[i]+prefix[k+i-n], result);
        }
        return result;
    }
}
// @lc code=end

