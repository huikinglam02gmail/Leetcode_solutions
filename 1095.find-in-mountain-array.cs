/*
 * @lc app=leetcode id=1095 lang=csharp
 *
 * [1095] Find in Mountain Array
 */

// @lc code=start
/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *     public int Get(int index) {}
 *     public int Length() {}
 * }
 */

/**
 * This is MountainArray's API interface.
 * You should not implement it, or speculate about its implementation
 */

class Solution {
    public int FindInMountainArray(int target, MountainArray mountainArr) 
    {
        int n = mountainArr.Length();
        int left = 0, right = n;
        int mid = -1;
        while (left < right)
        {
            mid = left + (right - left) / 2;
            int[] A = new int[] { mountainArr.Get(mid - 1), mountainArr.Get(mid), mountainArr.Get(mid + 1) };
            if (A[0] < A[1] && A[1] > A[2])
            {
                break;
            }
            else if (A[0] < A[1] && A[1] < A[2])
            {
                left = mid;
            }
            else
            {
                right = mid;
            }
        }

        left = 0;
        right = mid + 1;

        while (left < right)
        {
            mid = left + (right - left) / 2;
            int num = mountainArr.Get(mid);
            if (num == target)
            {
                return mid;
            }
            else if (num < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        if (left >= 0 && mountainArr.Get(left) == target)
        {
            return left;
        }

        left = mid;
        right = n;

        while (left < right)
        {
            mid = left + (right - left) / 2;
            int num = mountainArr.Get(mid);
            if (num == target)
            {
                return mid;
            }
            else if (num > target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        if (left < n && mountainArr.Get(left) == target)
        {
            return left;
        }

        return -1;   
    }
}

// @lc code=end

