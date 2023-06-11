/*
 * @lc app=leetcode id=1146 lang=csharp
 *
 * [1146] Snapshot Array
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class SnapshotArray
{
    private List<List<int[]>> history;
    private int snapCount;

    public SnapshotArray(int length)
    {
        history = new List<List<int[]>>(length);
        for (int i = 0; i < length; i++)
        {
            history.Add(new List<int[]> { new int[] { -1, 0 } });
        }
        snapCount = -1;
    }

    public void Set(int index, int val)
    {
        int[] lastEntry = history[index][history[index].Count - 1];
        int lastSnapId = lastEntry[0];
        if (lastSnapId == snapCount)
        {
            lastEntry[1] = val;
        }
        else
        {
            history[index].Add(new int[] { snapCount, val });
        }
    }

    public int Snap()
    {
        snapCount++;
        return snapCount;
    }

    public int Get(int index, int snapId)
    {
        List<int[]> snapHistory = history[index];
        int result = bisectRight(snapHistory.Select(x => x[0]).ToList(), snapId - 1);
        return snapHistory[result - 1][1];
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
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.Set(index,val);
 * int param_2 = obj.Snap();
 * int param_3 = obj.Get(index,snap_id);
 */
// @lc code=end

