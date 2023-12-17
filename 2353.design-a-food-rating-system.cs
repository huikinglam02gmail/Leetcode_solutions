/*
 * @lc app=leetcode id=2353 lang=csharp
 *
 * [2353] Design a Food Rating System
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class FoodRatings
{
    private Dictionary<string, PriorityQueue<string, Tuple<int, string>>> cuisineHashTable;
    private Dictionary<string, Tuple<int, string>> foodHashTable;

    public FoodRatings(string[] foods, string[] cuisines, int[] ratings)
    {
        cuisineHashTable = new Dictionary<string, PriorityQueue<string, Tuple<int, string>>>();
        foodHashTable = new Dictionary<string, Tuple<int, string>>();

        for (int i = 0; i < foods.Length; i++)
        {
            if (!cuisineHashTable.ContainsKey(cuisines[i]))
            {
                cuisineHashTable[cuisines[i]] = new PriorityQueue<string, Tuple<int, string>>();
            }

            cuisineHashTable[cuisines[i]].Enqueue(foods[i], new Tuple<int, string> (- ratings[i], foods[i]));
            foodHashTable[foods[i]] = new Tuple<int, string>(ratings[i], cuisines[i]);
        }
    }

    public void ChangeRating(string food, int newRating)
    {
        foodHashTable[food] = new Tuple<int, string>(newRating, foodHashTable[food].Item2);
        cuisineHashTable[foodHashTable[food].Item2].Enqueue(food, new Tuple<int, string> (- newRating, food));
    }

    public string HighestRated(string cuisine)
    {
        while (cuisineHashTable[cuisine].TryPeek(out string ele, out Tuple<int, string> t) && t.Item1 != - foodHashTable[ele].Item1)
        {
            cuisineHashTable[cuisine].Dequeue();
        }
        return cuisineHashTable[cuisine].Peek();
    }
}


/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * string param_2 = obj.HighestRated(cuisine);
 */
// @lc code=end

