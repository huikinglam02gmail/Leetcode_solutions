/*
 * @lc app=leetcode id=119 lang=csharp
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
public class Solution {
    public IList<int> GetRow(int rowIndex) {
        List<int> curr = new List<int> { 1 };
        int i = 0;
        while (i < rowIndex) {
            List<int> nxt = new List<int> { 1 };
            for (int j = 0; j < curr.Count - 1; j++) {
                nxt.Add(curr[j] + curr[j + 1]);
            }
            nxt.Add(1);
            curr = nxt;
            i++;
        }
        return curr;
    }
}
// @lc code=end

