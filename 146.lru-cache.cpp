/*
 * @lc app=leetcode id=146 lang=cpp
 *
 * [146] LRU Cache
 */

// @lc code=start
#include <iostream>
#include <unordered_map>
#include <list>
using namespace std;

class LRUCache
{
private:
    int capacity;
    unordered_map<int, list<pair<int, int>>::iterator> hashTable;
    list<pair<int, int>> q;

public:
    LRUCache(int capacity)
    {
        this->capacity = capacity;
    }

    int get(int key)
    {
        if (hashTable.find(key) == hashTable.end())
            return -1;
        else
        {
            q.splice(q.begin(), q, hashTable[key]);
            return hashTable[key]->second;
        }
    }

    void put(int key, int value)
    {
        if (hashTable.find(key) == hashTable.end())
        {
            if (q.size() == capacity)
            {
                hashTable.erase(q.back().first);
                q.pop_back();
            }
        }
        else
        {
            q.erase(hashTable[key]);
        }
        q.push_front({ key, value });
        hashTable[key] = q.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

