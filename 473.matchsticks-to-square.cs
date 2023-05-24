/*
 * @lc app=leetcode id=473 lang=csharp
 *
 * [473] Matchsticks to Square
 */

// @lc code=start
public class Solution 
{
    /*
    Can use DFS because n <= 16
    A greedy approach: allocate larger nums first to ones with more available space: sort nums from large to small and states from small to large
    To identify the state, we use dfs(i, stateString) = nums[i:] is left behind, current state "0_0_0_..._0" nothing assigned    
    */    

    Dictionary<Tuple<int, string>, bool> cache = new Dictionary<Tuple<int, string>, bool>();
    int[] Nums;
    int target;
    int K;
    public bool DFS(int i, string state)
    {
        Tuple<int, string> t = new Tuple<int, string>(i, state);
        bool result;
        if (cache.ContainsKey(t))
        {
            return cache[t];
        }
        else if (i == Nums.Length)
        {
            result = state.Split('_').All(s => Int32.Parse(s) == target);                
        }
        else
        {
            var stateList = state.Split('_').Select(s => Int32.Parse(s)).ToList();
            result = false;
            for (int l = 0; l < K; l++)
            {
                if (Nums[i] + stateList[l] <= target)
                {
                    stateList[l] += Nums[i];
                    string nextState = string.Join("_", stateList.OrderBy(j => j));
                    if (DFS(i + 1, nextState))
                    {
                        result = true;
                    }
                    stateList[l] -= Nums[i];
                }
            }
        }
        cache.Add(t, result);
        return result;
    }

    public bool CanPartitionKSubsets(int[] nums, int k)
    {
        int sum = nums.Sum();
        if (sum % k != 0 || nums.Max() > sum / k)
        {
            return false;            
        }
        else
        {
            target = sum / k;
            K = k;
            Nums = nums.OrderByDescending(n => n).ToArray();
            return DFS(0, string.Join("_", Enumerable.Repeat("0", k)));
        }
    }

    public bool Makesquare(int[] matchsticks) 
    {
        return CanPartitionKSubsets(matchsticks, 4);
    }
}
// @lc code=end

