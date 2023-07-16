/*
 * @lc app=leetcode id=1814 lang=csharp
 *
 * [1814] Count Nice Pairs in an Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
     * First prepare the second array rev(nums)
     * Then given the condition nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
     * nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
     * So we just maintain this difference and maintain a set
     */
    public int CountNicePairs(int[] nums) {
        Dictionary<int, HashSet<int>> hashTable = new Dictionary<int, HashSet<int>>();
        long result = 0;
        long MOD = 1000000007;

        for (int i = 0; i < nums.Length; i++) {
            int num = nums[i];
            int diff = num - ReverseNumber(num);
            if (!hashTable.ContainsKey(diff)) {
                hashTable[diff] = new HashSet<int>();
            }
            hashTable[diff].Add(i);
        }

        foreach (HashSet<int> v in hashTable.Values) {
            long count = Convert.ToInt64(v.Count);
            result += count * (count - 1) / 2;
            result %= MOD;
        }

        return Convert.ToInt32(result);
    }

    private int ReverseNumber(int num) {
        int reversed = 0;
        while (num > 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }
        return reversed;
    }
}

// @lc code=end

