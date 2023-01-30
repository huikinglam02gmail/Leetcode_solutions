/*
 * @lc app=leetcode id=460 lang=csharp
 *
 * [460] LFU Cache
 */

// @lc code=start
using System.Collections.Specialized;
public class LFUCache 
{
    int Capacity;
    int minFreq;
    Dictionary<int, int> keyFreq;
    Dictionary<int, OrderedDictionary> freqKeys;
    public LFUCache(int capacity) 
    {    
        Capacity = capacity;
        minFreq = 0;
        keyFreq = new Dictionary<int, int>();
        freqKeys = new Dictionary<int, OrderedDictionary>();
    }
    
    public void maintenance(int key)
    {
        int freq = keyFreq[key];
        int val = (int) freqKeys[freq][(object) key];

        freqKeys[freq].Remove(key);
        if (freqKeys[freq].Count == 0 && freq == minFreq)
        {
            minFreq++;
            freqKeys.Remove(freq);
        }
        keyFreq[key]++;
        if (!freqKeys.ContainsKey(freq + 1))
        {
            freqKeys.Add(freq + 1, new OrderedDictionary());
        }
        freqKeys[freq + 1].Add(key, val);
    }

    public int Get(int key) 
    {
        if (!keyFreq.ContainsKey(key))
        {
            return -1;
        }
        else
        {
            maintenance(key);
            return (int) freqKeys[keyFreq[key]][(object) key];
        }
        
    }
    
    public void Put(int key, int value) 
    {
        if (Capacity > 0)
        {        
            if (keyFreq.ContainsKey(key))
            {
                freqKeys[keyFreq[key]][(object) key] = value;
            }
            else
            {
                if (Capacity == keyFreq.Count)
                {
                    int keyToDelete = (int) freqKeys[minFreq].Cast<DictionaryEntry>().ElementAt(0).Key;
                    freqKeys[minFreq].Remove(keyToDelete);
                    keyFreq.Remove(keyToDelete);
                }
                minFreq = 0;
                keyFreq.Add(key, minFreq);
                freqKeys.Add(minFreq, new OrderedDictionary());
                freqKeys[minFreq].Add(key, value);
            }
            maintenance(key);
        } 
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end

