/*
 * @lc app=leetcode id=1649 lang=csharp
 *
 * [1649] Create Sorted Array through Instructions
 */

// @lc code=start
public class sumSegmentTree
{
    public int[] tree;
    public sumSegmentTree(int size, int initialValue)
    {
        tree = new int[size];
        Array.Fill(tree, initialValue);
    }

    public void update(int i, int val)
    {
        i += tree.Length / 2;
        tree[i] += val;
        i = i / 2;
        while (i > 0)
        {
            tree[i] = tree[2*i] + tree[2*i + 1];
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
                res += tree[start];
                start++;
            }
            if (end % 2 == 0)
            {
                res += tree[end];
                end--;
            }
            start /= 2;
            end /= 2;
        }
        return res;
    }
}


public class Solution {
    long MOD = 1000000007;
    public int CreateSortedArray(int[] instructions) 
    {
        sumSegmentTree Tree = new sumSegmentTree(200002, 0);
        long result = 0;
        for (int i = 0; i < instructions.Length; i++)
        {
            result += Math.Min(Tree.query(0, instructions[i] - 1), Tree.query(instructions[i] + 1, 100000));
            result %= MOD;
            Tree.update(instructions[i], 1);
        }
        return Convert.ToInt32(result);
    }
}
// @lc code=end

