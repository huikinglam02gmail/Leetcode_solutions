/*
 * @lc app=leetcode id=706 lang=csharp
 *
 * [706] Design HashMap
 */

// @lc code=start
public class MyHashMap
{
    private List<(int, int)>[] arr;

    public MyHashMap()
    {
        arr = new List<(int, int)>[1 << 15];
        for (int i = 0; i < (1 << 15); i++)
        {
            arr[i] = new List<(int, int)>();
        }
    }

    public int EvalHash(int key)
    {
        return ((key * 1031231) & ((1 << 20) - 1)) >> 5;
    }

    public void Put(int key, int value)
    {
        int t = EvalHash(key);
        for (int i = 0; i < arr[t].Count; i++)
        {
            if (arr[t][i].Item1 == key)
            {
                arr[t][i] = (key, value);
                return;
            }
        }
        arr[t].Add((key, value));
    }

    public int Get(int key)
    {
        int t = EvalHash(key);
        for (int i = 0; i < arr[t].Count; i++)
        {
            if (arr[t][i].Item1 == key)
            {
                return arr[t][i].Item2;
            }
        }
        return -1;
    }

    public void Remove(int key)
    {
        int t = EvalHash(key);
        for (int i = 0; i < arr[t].Count; i++)
        {
            if (arr[t][i].Item1 == key)
            {
                arr[t].RemoveAt(i);
                return;
            }
        }
    }
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.Put(key,value);
 * int param_2 = obj.Get(key);
 * obj.Remove(key);
 */
// @lc code=end

