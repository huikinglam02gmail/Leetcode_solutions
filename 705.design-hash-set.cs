/*
 * @lc app=leetcode id=705 lang=csharp
 *
 * [705] Design HashSet
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class MyHashSet
{
    private List<int>[] arr;

    public MyHashSet()
    {
        arr = new List<int>[1 << 15];
        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] = new List<int>();
        }
    }

    private int EvalHash(int key)
    {
        return ((key * 1031231) & ((1 << 20) - 1)) >> 5;
    }

    public void Add(int key)
    {
        int t = EvalHash(key);
        if (!arr[t].Contains(key))
        {
            arr[t].Add(key);
        }
    }

    public void Remove(int key)
    {
        int t = EvalHash(key);
        if (arr[t].Contains(key))
        {
            arr[t].Remove(key);
        }
    }

    public bool Contains(int key)
    {
        int t = EvalHash(key);
        return arr[t].Contains(key);
    }
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.Add(key);
 * obj.Remove(key);
 * bool param_3 = obj.Contains(key);
 */
// @lc code=end

