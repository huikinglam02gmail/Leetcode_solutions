/*
 * @lc app=leetcode id=2353 lang=cpp
 *
 * [2353] Design a Food Rating System
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>

class FoodRatings {
private:
    using Pair = std::pair<int, std::string>;
    using PriorityQueue = std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>>;

    std::unordered_map<std::string, PriorityQueue> cuisineHashTable;
    std::unordered_map<std::string, Pair> foodHashTable;

public:
    FoodRatings(const std::vector<std::string>& foods, const std::vector<std::string>& cuisines, const std::vector<int>& ratings) {
        for (std::size_t i = 0; i < foods.size(); ++i) {
            if (cuisineHashTable.find(cuisines[i]) == cuisineHashTable.end()) {
                cuisineHashTable[cuisines[i]] = PriorityQueue();
            }

            cuisineHashTable[cuisines[i]].emplace(-ratings[i], foods[i]);
            foodHashTable[foods[i]] = std::make_pair(ratings[i], cuisines[i]);
        }
    }

    void changeRating(const std::string& food, int newRating) {
        foodHashTable[food].first = newRating;
        cuisineHashTable[foodHashTable[food].second].emplace(-newRating, food);
    }

    std::string highestRated(const std::string& cuisine) {
        while (!cuisineHashTable[cuisine].empty() && foodHashTable[cuisineHashTable[cuisine].top().second].first != -cuisineHashTable[cuisine].top().first) {
            cuisineHashTable[cuisine].pop();
        }
        return cuisineHashTable[cuisine].top().second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
// @lc code=end

