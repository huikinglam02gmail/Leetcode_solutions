/*
 * @lc app=leetcode id=1787 lang=csharp
 *
 * [1787] Make the XOR of All Segments Equal to Zero
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    For all segments (subarray of size k) with XOR = j, it means nums[i] == nums[i + k].
    Therefore we should record the occurrences of nums[i], nums[i + k], ... etc, and put them in a dictionary list of size k.
    Then the question becomes, in each group, which number should I choose to represent the group.
    Notice it is possible that among the existing numbers, we cannot reach a total XOR of 0, as in Example 3.
    Given we choose num_1... num_k, what if they do not XOR together to 0?
    So we find the group j in which occur[j][num_j] is the minimum among different groups.
    This group can be replaced by 0^num_1^...^num_(j - 1)^num_(j + 1)^...^num_k.
    How about the case in Example 1 & 2, where we can choose the final number from the given groups?
    Then we DP on the groups:
    dp[j][XS] = after considering groups[:j + 1], what are the number of elements within groups[:j + 1] that would contribute to the final XOR sum of XS.
    We are looking for dp[n - 1][0].
    */

    public int MinChanges(int[] nums, int k) {
        Dictionary<int, int>[] occur = new Dictionary<int, int>[k];
        for (int i = 0; i < k; i++) {
            occur[i] = new Dictionary<int, int>();
        }
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            int key = i % k;
            if (!occur[key].ContainsKey(nums[i])) {
                occur[key][nums[i]] = 0;
            }
            occur[key][nums[i]]++;
        }

        Dictionary<int, int> dp = occur[0];
        for (int i = 1; i < k; i++) {
            Dictionary<int, int> dpNew = new Dictionary<int, int>();
            foreach (KeyValuePair<int, int> kvp in occur[i]) {
                foreach (KeyValuePair<int, int> kvp2 in dp) {
                    int xor = kvp2.Key ^ kvp.Key;
                    dpNew[xor] = Math.Max(dpNew.ContainsKey(xor) ? dpNew[xor] : 0, kvp.Value + kvp2.Value);
                }
            }
            dp = dpNew;
        }

        int maxOccur = dp.ContainsKey(0) ? dp[0] : 0;
        int maxOccurSum = 0;
        int minOccurSum = int.MaxValue;
        foreach (Dictionary<int, int> dict in occur) {
            int maxCount = 0;
            foreach (KeyValuePair<int, int> kvp in dict) {
                maxCount = Math.Max(maxCount, kvp.Value);
            }
            maxOccurSum += maxCount;
            minOccurSum = Math.Min(minOccurSum, maxCount);
        }

        return n - Math.Max(maxOccur, maxOccurSum - minOccurSum);
    }
}
// @lc code=end

