/*
 * @lc app=leetcode id=1865 lang=csharp
 *
 * [1865] Finding Pairs With a Certain Sum
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class FindSumPairs {
    private Dictionary<int, int> hashTable;
    private int[] nums1;
    private int[] nums2;

    public FindSumPairs(int[] nums1, int[] nums2) {
        hashTable = new Dictionary<int, int>();
        this.nums1 = nums1;
        this.nums2 = nums2;
        foreach (int num in nums2) {
            if (!hashTable.ContainsKey(num)) {
                hashTable[num] = 1;
            }
            else {
                hashTable[num]++;
            }
        }
    }

    public void Add(int index, int val) {
        hashTable[nums2[index]]--;
        int newNum = nums2[index] + val;
        if (!hashTable.ContainsKey(newNum)) {
            hashTable[newNum] = 1;
        }
        else {
            hashTable[newNum]++;
        }
        nums2[index] = newNum;
    }

    public int Count(int tot) {
        int result = 0;
        foreach (int num1 in nums1) {
            int target = tot - num1;
            if (hashTable.ContainsKey(target)) {
                result += hashTable[target];
            }
        }
        return result;
    }
}


/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.Add(index,val);
 * int param_2 = obj.Count(tot);
 */
// @lc code=end

