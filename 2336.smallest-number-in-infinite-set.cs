/*
 * @lc app=leetcode id=2336 lang=csharp
 *
 * [2336] Smallest Number in Infinite Set
 */

// @lc code=start
using System.Collections.Generic;
public class SmallestInfiniteSet 
{
    HashSet<int> lost;
    int smallest;
    public SmallestInfiniteSet() 
    {
        lost = new HashSet<int>();
        smallest = 1;
    }
    
    public int PopSmallest() 
    {
        int item = smallest;
        lost.Add(item);
        while (lost.Contains(smallest))
        {
            smallest++;
        }
        return item;
    }
    
    public void AddBack(int num) 
    {
        if (lost.Contains(num))
        {
            lost.Remove(num);
        }
        if (num < smallest)
        {
            smallest = num;
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.PopSmallest();
 * obj.AddBack(num);
 */
// @lc code=end

