/*
 * @lc app=leetcode id=1574 lang=csharp
 *
 * [1574] Shortest Subarray to be Removed to Make Array Sorted
 */

// @lc code=start
public class Solution 
{
    public int bisectLeft(List<int> nums, int target)
    {
        int left = 0;
        int right = nums.Count;
        int mid;

        while (left < right)
        {
            mid = left + (right - left) / 2;
            if (nums[mid] < target)
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

    public int FindLengthOfShortestSubarray(int[] arr)
    {
        int n = arr.Length;
        int left;
        int right;
        int nl;
        int nr;
        int mid;
        List<int> leftSubarray = new List<int>() {arr[0]};
        List<int> rightSubarray = new List<int>();
        Stack<int> rightStack = new Stack<int>();
        rightStack.Push(arr[arr.Length - 1]);
        int p = 0;
        while (p < n - 1 && arr[p] <= arr[p + 1])
        {
            p++;
            leftSubarray.Add(arr[p]);
        }
        left = n - p - 1;
        if (left == 0)
        {
            return 0;
        }

        p = n - 1;
        while (p > 0 && arr[p - 1] <= arr[p])
        {
            p--;
            rightStack.Push(arr[p]);
        }
        right = p;

        while (rightStack.TryPop(out int item))
        {
            rightSubarray.Add(item);
        }

        nl = leftSubarray.Count;
        nr = rightSubarray.Count;
        mid = Math.Min(left, right);
        for (int i = 0; i < nl; i++)
        {
            int ind = bisectLeft(rightSubarray, leftSubarray[i]);
            mid = Math.Min(mid, n - i - 1 - nr + ind);
        }
        return mid;
    }
}
// @lc code=end

