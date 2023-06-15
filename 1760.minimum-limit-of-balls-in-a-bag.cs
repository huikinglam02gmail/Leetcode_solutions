/*
 * @lc app=leetcode id=1760 lang=csharp
 *
 * [1760] Minimum Limit of Balls in a Bag
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    1 <= maxOperations, nums[i] <= 10^9: we know using a priority queue is not a good idea.
    Let's frame the question differently: suppose 'ans' is the solution. How many operations are needed to get there?
    Suppose we have nums[i] = 8 and 'ans' is 3.
    The division procedure that minimizes operations is: 8 -> [3, 5] -> [3, 3, 2], with 2 = 8 // 3 operations.
    And we know that as 'ans' increases, the number of operations decreases.
    So, binary search is the answer to this question.
    */

    private int OperationsToMake(int maxN, int[] nums)
    {
        int result = 0;
        foreach (int num in nums)
        {
            result += num / maxN;
            if (num % maxN == 0)
            {
                result -= 1;
            }
        }
        return result;
    }

    public int MinimumSize(int[] nums, int maxOperations)
    {
        int l = 1;
        int r = nums.Max();

        while (l < r)
        {
            int mid = l + (r - l) / 2;
            if (OperationsToMake(mid, nums) <= maxOperations)
            {
                r = mid;
            }
            else
            {
                l = mid + 1;
            }
        }

        return l;
    }
}
// @lc code=end

