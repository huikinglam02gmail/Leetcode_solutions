/*
 * @lc app=leetcode id=2080 lang=csharp
 *
 * [2080] Range Frequency Queries
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class RangeFreqQuery {
    private Dictionary<int, List<int>> appear;

    public RangeFreqQuery(int[] arr) {
        appear = new Dictionary<int, List<int>>();
        for (int i = 0; i < arr.Length; i++) {
            if (!appear.ContainsKey(arr[i])) {
                appear[arr[i]] = new List<int>();
            }
            appear[arr[i]].Add(i);
        }
    }

    public int Query(int left, int right, int value) {
        if (!appear.ContainsKey(value)) {
            return 0;
        } else {
            int leftIndex = BinarySearchLeft(appear[value], left);
            int rightIndex = BinarySearchRight(appear[value], right);
            return rightIndex - leftIndex;
        }
    }

    private int BinarySearchLeft(List<int> list, int target) {
        int left = 0;
        int right = list.Count;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (list[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    private int BinarySearchRight(List<int> list, int target) {
        int left = 0;
        int right = list.Count;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (list[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}


/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = new RangeFreqQuery(arr);
 * int param_1 = obj.Query(left,right,value);
 */
// @lc code=end

