/*
 * @lc app=leetcode id=31 lang=csharp
 *
 * [31] Next Permutation
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
     * A good example is [1,2,4,3]
     * Find the first instance in which nums[i] < nums[i+1]
     * That's the index in which one can exchange between later index
     * -> index 2
     * Then we swap the one element before this index with the rightmost element which is larger than this element
     * [1, 3, 4, 2]
     * finally, we swap everything element between left + 1 and right
     * If the sequence is non-increasing, we swap the whole sequence
     */
    public void NextPermutation(int[] nums)
    {
        int n = nums.Length;
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1])
        {
            i--;
        }

        if (i >= 0)
        {
            int j = n - 1;
            while (j > i && nums[i] >= nums[j])
            {
                j--;
            }
            // exchange
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }

        i++;
        int k = n - 1;
        while (i < k)
        {
            int temp = nums[i];
            nums[i] = nums[k];
            nums[k] = temp;
            i++;
            k--;
        }
    }
}

// @lc code=end

