/*
 * @lc app=leetcode id=2407 lang=csharp
 *
 * [2407] Longest Increasing Subsequence II
 */

// @lc code=start
public class maxSegmentTree
{
    public int[] tree;
    public maxSegmentTree(int size, int initialValue)
    {
        tree = new int[size];
        Array.Fill(tree, initialValue);
    }

    public void update(int i, int val)
    {
        i += tree.Length / 2;
        tree[i] = val;
        i = i / 2;
        while (i > 0)
        {
            tree[i] = Math.Max(tree[2*i], tree[2*i + 1]);
            i = i / 2;
        }
    }

    public int query(int start, int end)
    {
        start += tree.Length / 2;
        end += tree.Length / 2;
        int res = 0;
        while (start <= end)
        {
            if (start % 2 == 1)
            {
                res = Math.Max(res, tree[start]);
                start++;
            }
            if (end % 2 == 0)
            {
                res = Math.Max(res, tree[end]);
                end--;
            }
            start /= 2;
            end /= 2;
        }
        return res;
    }
}
public class Solution 
{
    public int LengthOfLIS(int[] nums, int k) 
    {
        int result = 0;
        maxSegmentTree dp = new maxSegmentTree(2*(nums.Max() + 1), 0);

        foreach (int num in nums)
        {
            int start = Math.Max(0, num - k);
            int end = num - 1;
            int maxDP = dp.query(start, end) + 1;
            result = Math.Max(result, maxDP);
            dp.update(num, maxDP);
        }   
        return result; 
    }
}
// @lc code=end

