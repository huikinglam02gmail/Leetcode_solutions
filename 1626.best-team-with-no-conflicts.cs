/*
 * @lc app=leetcode id=1626 lang=csharp
 *
 * [1626] Best Team With No Conflicts
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
    public int BestTeamScore(int[] scores, int[] ages) 
    {
        maxSegmentTree dp = new maxSegmentTree(2*(1 + ages.Max()), 0);
        List<int[]> data = new List<int[]>();
        int result = 0;
        for (int i = 0; i < ages.Length; i++)
        {
            data.Add(new int[2] {scores[i], ages[i]});
        }
        data = data.OrderBy(x => x[0]).ThenBy(x => x[1]).ToList();

        foreach (int[] datum in data)
        {
            int newMaxTotalScoreCandidate = datum[0] + dp.query(0, datum[1]);
            result = Math.Max(result, newMaxTotalScoreCandidate);
            dp.update(datum[1], newMaxTotalScoreCandidate);
        }
        return result;
    }
}
// @lc code=end

