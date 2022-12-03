/*
 * @lc app=leetcode id=1508 lang=csharp
 *
 * [1508] Range Sum of Sorted Subarray Sums
 */

// @lc code=start
public class Solution 
{
    long[] prefix;
    long[] prePrefix;
    int N;
    long MOD = 1000000007;

    public long countSubArraySumBelowS(long S)
    {
        long count = 0;
        int i = 0;
        for (int j = 0; j < N + 1; j++)
        {
            while (prefix[j] - prefix[i] > S)
            {
                i++;
            }
            count += j - i;
        }
        return count;
    }

    public long subarraySumGiveIndex(long ind)
    {
        long l = 0;
        long r = prefix[prefix.Length - 1];
        while (l < r)
        {
            long mid = (l + r) / 2;
            if (countSubArraySumBelowS(mid) < ind)
            {
                l = mid + 1;
            }
            else
            {
                r = mid;
            }
        }
        return l;
    }

    public long sumAllSubArraysUpToIndex(int ind)
    {
        long S = subarraySumGiveIndex(ind);
        long result = 0;
        int i = 0;
        for (int j = 0; j < N + 1; j++)
        {
            while (prefix[j] - prefix[i] > S)
            {
                i++;
            }
            result += prefix[j]*(j - i + 1) - prePrefix[j];
            if (i > 0)
            {
                result += prePrefix[i - 1];
            }
        }
        return result - (countSubArraySumBelowS(S) - ind)*S;
    }

    public int RangeSum(int[] nums, int n, int left, int right) 
    {
        prefix = new long[n + 1];
        prePrefix = new long[n + 1];
        N = n;
        prefix[0] = 0;
        prePrefix[0] = 0;
        for (int i = 0; i < N; i++)
        {
            prefix[i + 1] = prefix[i] + nums[i];
            prePrefix[i + 1] = prePrefix[i] + prefix[i + 1];
        }
        return Convert.ToInt32((sumAllSubArraysUpToIndex(right) - sumAllSubArraysUpToIndex(left - 1)) % MOD);
    }
}
// @lc code=end

