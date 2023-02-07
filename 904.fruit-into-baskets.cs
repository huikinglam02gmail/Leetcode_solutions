/*
 * @lc app=leetcode id=904 lang=csharp
 *
 * [904] Fruit Into Baskets
 */

// @lc code=start
public class Solution 
{
    public int TotalFruit(int[] fruits) 
    {
        int i = 0;    
        int result = 0;
        Dictionary<int, int> basket = new Dictionary<int, int>();
        for (int j = 0; j < fruits.Length; j++)
        {
            if (!basket.ContainsKey(fruits[j]))
            {
                basket.Add(fruits[j], 0);
            }
            basket[fruits[j]]++;
            while (basket.Count > 2)
            {
                basket[fruits[i]]--;
                if (basket[fruits[i]] == 0)
                {
                    basket.Remove(fruits[i]);
                }
                i++;
            }
            result = Math.Max(result, j - i + 1);
        }
        return result;
    }
}
// @lc code=end

