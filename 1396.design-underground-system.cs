/*
 * @lc app=leetcode id=1396 lang=csharp
 *
 * [1396] Design Underground System
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class UndergroundSystem
{
    private Dictionary<int, Tuple<string, int>> customers;
    private Dictionary<Tuple<string, string>, Tuple<int, int>> travelTimes;

    public UndergroundSystem()
    {
        customers = new Dictionary<int, Tuple<string, int>>();
        travelTimes = new Dictionary<Tuple<string, string>, Tuple<int, int>>();
    }

    public void CheckIn(int id, string stationName, int t)
    {
        if (!customers.ContainsKey(id))
        {
            customers[id] = new Tuple<string, int>("", 0);
        }
        customers[id] = new Tuple<string, int>(stationName, t);
    }

    public void CheckOut(int id, string stationName, int t)
    {
        Tuple<string, int> customer = customers[id];
        string startName = customer.Item1;
        int startTime = customer.Item2;

        Tuple<string, string> key = new Tuple<string, string>(startName, stationName);

        if (!travelTimes.ContainsKey(key))
        {
            travelTimes[key] = new Tuple<int, int>(0, 0);
        }

        Tuple<int, int> value = travelTimes[key];
        int totalTime = value.Item1 + (t - startTime);
        int totalRides = value.Item2 + 1;

        travelTimes[key] = new Tuple<int, int>(totalTime, totalRides);

        customers[id] = new Tuple<string, int>("", 0);
    }

    public double GetAverageTime(string startStation, string endStation)
    {
        Tuple<int, int> value = travelTimes[new Tuple<string, string>(startStation, endStation)];
        int totalTime = value.Item1;
        int totalRides = value.Item2;

        return (double)totalTime / totalRides;
    }
}


/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * double param_3 = obj.GetAverageTime(startStation,endStation);
 */
// @lc code=end

