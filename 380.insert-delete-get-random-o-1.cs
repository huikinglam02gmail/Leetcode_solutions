/*
 * @lc app=leetcode id=380 lang=csharp
 *
 * [380] Insert Delete GetRandom O(1)
 */

// @lc code=start
public class RandomizedSet 
{
    Dictionary<int, int> hashTable;
    List<int> arr;

    public RandomizedSet() 
    {
        hashTable = new Dictionary<int, int>();
        arr = new List<int>();
    }
    
    public bool Insert(int val) 
    {
        bool result = !hashTable.ContainsKey(val);
        if (result)
        {
            arr.Add(val);
            hashTable.Add(val, arr.Count - 1);
        }
        return result;
    }
    
    public bool Remove(int val) 
    {
        bool result = hashTable.ContainsKey(val);
        if (result)
        {
            int x = arr[arr.Count - 1];
            arr.RemoveAt(arr.Count - 1);
            if (x != val)
            {
                arr[hashTable[val]] = x;
                hashTable[x] = hashTable[val];
            }
            hashTable.Remove(val);
        }
        return result;
    }
    
    public int GetRandom()
    {
        Random rnd = new Random();
        return arr[rnd.Next(0, arr.Count)];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
// @lc code=end

