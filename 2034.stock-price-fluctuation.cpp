/*
 * @lc app=leetcode id=2034 lang=cpp
 *
 * [2034] Stock Price Fluctuation 
 */

// @lc code=start
#include <iostream>
#include <unordered_map>
#include <queue>

class StockPrice {
public:
    int latestTime;
    std::priority_queue<std::pair<int, int>> maxHeap;    // max heap
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap; // min heap
    std::unordered_map<int, int> hashTable;

    StockPrice() {
        latestTime = 0;
    }

    void update(int timestamp, int price) {
        latestTime = std::max(latestTime, timestamp);
        hashTable[timestamp] = price;
        maxHeap.push({price, timestamp});
        minHeap.push({price, timestamp});
    }

    int current() {
        return hashTable[latestTime];
    }

    int maximum() {
        while (!maxHeap.empty() && hashTable[maxHeap.top().second] != maxHeap.top().first) {
            maxHeap.pop();
        }
        return maxHeap.top().first;
    }

    int minimum() {
        while (!minHeap.empty() && hashTable[minHeap.top().second] != minHeap.top().first) {
            minHeap.pop();
        }
        return minHeap.top().first;
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */
// @lc code=end

