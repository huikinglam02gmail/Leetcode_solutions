/*
 * @lc app=leetcode id=2034 lang=csharp
 *
 * [2034] Stock Price Fluctuation 
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class StockPrice {
    private int latestTime;
    private PriorityQueue<int, int> maxHeap;
    private PriorityQueue<int, int> minHeap;
    private Dictionary<int, int> hashTable;

    public StockPrice() {
        latestTime = 0;
        maxHeap = new PriorityQueue<int, int>();
        minHeap = new PriorityQueue<int, int>();
        hashTable = new Dictionary<int, int>();
    }

    public void Update(int timestamp, int price) {
        latestTime = Math.Max(latestTime, timestamp);
        hashTable[timestamp] = price;
        maxHeap.Enqueue(timestamp, - price);
        minHeap.Enqueue(timestamp, price);
    }

    public int Current() {
        return hashTable[latestTime];
    }

    public int Maximum() {
        while (maxHeap.TryPeek(out int timestamp, out int negPrice) && hashTable[timestamp] != - negPrice) {
            maxHeap.Dequeue();
        }
        if (maxHeap.TryPeek(out int timeStamp, out int Negprice)) return - Negprice;
        return 0;
    }

    public int Minimum() {
        while (minHeap.TryPeek(out int timestamp, out int Price) && hashTable[timestamp] != Price) {
            minHeap.Dequeue();
        }
        if (minHeap.TryPeek(out int timeStamp, out int price)) return price;
        return 0;
    }
}


/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.Update(timestamp,price);
 * int param_2 = obj.Current();
 * int param_3 = obj.Maximum();
 * int param_4 = obj.Minimum();
 */
// @lc code=end

