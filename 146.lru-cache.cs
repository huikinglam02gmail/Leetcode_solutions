/*
 * @lc app=leetcode id=146 lang=csharp
 *
 * [146] LRU Cache
 */

// @lc code=start
using System.Collections.Generic;

public class LRUCache
{
    private int capacity;
    private Dictionary<int, LinkedListNode<int[]>> hashTable;
    private LinkedList<int[]> q;

    public LRUCache(int capacity)
    {
        this.capacity = capacity;
        q = new LinkedList<int[]>();
        hashTable = new Dictionary<int, LinkedListNode<int[]>>();
    }

    public int Get(int key)
    {
        if (!hashTable.ContainsKey(key))
            return -1;
        else
        {
            q.Remove(hashTable[key]);
            q.AddFirst(hashTable[key]);
            return hashTable[key].Value[1];
        }
    }

    public void Put(int key, int value)
    {
        if (!hashTable.ContainsKey(key))
        {
            if (q.Count == capacity)
            {
                hashTable.Remove(q.Last.Value[0]);
                q.RemoveLast();
            }
        }
        else
        {
            q.Remove(hashTable[key]);
        }
        hashTable[key] = new LinkedListNode<int[]>(new int[] { key, value });
        q.AddFirst(hashTable[key]);
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end

