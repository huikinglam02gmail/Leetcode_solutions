/*
 * @lc app=leetcode id=1146 lang=cpp
 *
 * [1146] Snapshot Array
 */

// @lc code=start
/* We cannot use vector<int> here as binary search on a certain index is not available. Instead, we store that the info in a Map, with snapCount as key and val as value*/

#include <vector>
#include <map>
using std::map;
using std::vector;

class SnapshotArray 
{
private:
    int snapCount;
    vector<map<int, int>> history;

public:
    SnapshotArray(int length) 
    {
        for (int i = 0; i < length; i++)
        {
            map<int, int> row;
            row[-1] = 0;
            history.push_back(row);
        }
        snapCount = -1;
    }
    
    void set(int index, int val) 
    {
        history[index][snapCount] = val;
    }
    
    int snap() 
    {
        return ++snapCount;
    }
    
    int get(int index, int snap_id) 
    {
        return (--history[index].upper_bound(snap_id - 1))->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
// @lc code=end

