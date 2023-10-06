/*
 * @lc app=leetcode id=1930 lang=csharp
 *
 * [1930] Unique Length-3 Palindromic Subsequences
 */

// @lc code=start
public class Solution {
    public static int bisectLeft<T>(IList<T> arr, T x, int lo=0, int hi=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
        {
            hi = (hi == -1) ? arr.Count : hi;
            while (lo < hi)
            {
                int mid = lo + (hi - lo) / 2;
                if (arr[mid].CompareTo(x) < 0)
                {
                    lo = mid + 1;
                }
                else
                {
                    hi = mid;
                }
            }
            return lo;     
        }

        public static int bisectRight<T>(IList<T> nums, T target, int left=0, int right=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
        {
            right = (right == -1) ? nums.Count : right;
            while (left < right)
            {
                int mid = left + (right - left) / 2;

                if (nums[mid].CompareTo(target) <= 0)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid;
                }
            }
            return left;
        }

    public int CountPalindromicSubsequence(string s) {
        List<int>[] occur = new List<int>[26];
        for (int i = 0; i < 26; i++) {
            occur[i] = new List<int>();
        }
        
        for (int i = 0; i < s.Length; i++) {
            int index = s[i] - 'a';
            occur[index].Add(i);
        }
        
        int result = 0;
        for (int i = 0; i < 26; i++) {
            if (occur[i].Count > 1) {
                for (int j = 0; j < 26; j++) {
                    int left = bisectRight<int>(occur[j], occur[i][0]);
                    int right = bisectLeft<int>(occur[j], occur[i][occur[i].Count - 1]);
                    if (left != right) {
                        result++;
                    }
                }
            }
        }
        
        return result;
    }
}
// @lc code=end

