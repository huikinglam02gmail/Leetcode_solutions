/*
 * @lc app=leetcode id=321 lang=csharp
 *
 * [321] Create Maximum Number
 */

// @lc code=start
public class Solution {
    public int[] MostCompetitive(int[] nums, int k) {
        List<int> stack = new List<int>();
        int n = nums.Length;
        
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[i] > stack[stack.Count - 1] && n - i + stack.Count - 1 >= k) {
                stack.RemoveAt(stack.Count - 1);
            }
            stack.Add(nums[i]);
        }
        
        return stack.Take(k).ToArray();
    }

    public int[] MergeSubsequences(int[] seq1, int[] seq2) {
        List<int> result = new List<int>();
        int i = 0, j = 0;

        while (i < seq1.Length && j < seq2.Length) {
            if (seq1[i] > seq2[j]) {
                result.Add(seq1[i]);
                i++;
            } else if (seq1[i] < seq2[j]) {
                result.Add(seq2[j]);
                j++;
            } else {
                int i1 = i + 1, j1 = j + 1;

                while (i1 < seq1.Length && j1 < seq2.Length && seq1[i1] == seq2[j1]) {
                    i1++;
                    j1++;
                }

                if (i1 == seq1.Length || (j1 < seq2.Length && seq1[i1] < seq2[j1])) {
                    result.Add(seq2[j]);
                    j++;
                } else {
                    result.Add(seq1[i]);
                    i++;
                }
            }
        }

        while (i < seq1.Length) {
            result.Add(seq1[i]);
            i++;
        }

        while (j < seq2.Length) {
            result.Add(seq2[j]);
            j++;
        }

        return result.ToArray();
    }

    public int[] FindMax(int[] result1, int[] result2) {
        int n = result1.Length;

        for (int i = 0; i < n; i++) {
            if (result1[i] > result2[i]) {
                return result1;
            } else if (result1[i] < result2[i]) {
                return result2;
            }
        }

        return result1;
    }

    public int[] MaxNumber(int[] nums1, int[] nums2, int k) {
        int useOneLowerLimit = Math.Max(0, k - nums2.Length);
        int useOneUpperLimit = Math.Min(nums1.Length, k);
        int[] result = new int[k];

        for (int i = useOneLowerLimit; i <= useOneUpperLimit; i++) {
            int[] nums1MaxSubSeq = MostCompetitive(nums1, i);
            int[] nums2MaxSubSeq = MostCompetitive(nums2, k - i);
            int[] current = MergeSubsequences(nums1MaxSubSeq, nums2MaxSubSeq);
            result = FindMax(result, current);
        }

        return result;
    }
}

// @lc code=end

