/*
 * @lc app=leetcode id=706 lang=cpp
 *
 * [706] Design HashMap
 */

// @lc code=start
#include <vector>
#include <list>

class MyHashMap {
private:
    std::vector<std::list<std::pair<int, int>>> arr;

    int evalHash(int key) {
        return ((static_cast<long long>(key) * 1031231) & ((1 << 20) - 1)) >> 5;
    }

public:
    MyHashMap() {
        arr.resize(1 << 15);
    }

    void put(int key, int value) {
        int t = evalHash(key);
        for (auto &entry : arr[t]) {
            if (entry.first == key) {
                entry.second = value;
                return;
            }
        }
        arr[t].emplace_back(key, value);
    }

    int get(int key) {
        int t = evalHash(key);
        for (const auto &entry : arr[t]) {
            if (entry.first == key) {
                return entry.second;
            }
        }
        return -1;
    }

    void remove(int key) {
        int t = evalHash(key);
        for (auto it = arr[t].begin(); it != arr[t].end(); ++it) {
            if (it->first == key) {
                arr[t].erase(it);
                return;
            }
        }
    }
};


/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
// @lc code=end

