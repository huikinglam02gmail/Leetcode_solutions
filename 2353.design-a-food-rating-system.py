#
# @lc app=leetcode id=2353 lang=python3
#
# [2353] Design a Food Rating System
#

# @lc code=start
import heapq
from typing import List


class FoodRatings:
    '''
    Notice: All the strings in foods are distinct
    Use a hash table to map cuisine to a max heap of food
    Use another hash table to map food to rating and cuisine
    When getting stuff from highest rating, we can lazily update the heap of the corresponding cusine to check if the rating correspond to that type of food    
    '''

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_hash_table = {}
        self.food_hash_table = {}
        for i in range(len(foods)):
            if cuisines[i] not in self.cuisine_hash_table:
                self.cuisine_hash_table[cuisines[i]] = []
            heapq.heappush(self.cuisine_hash_table[cuisines[i]],[-ratings[i], foods[i]])
            self.food_hash_table[foods[i]] = [ratings[i], cuisines[i]]

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_hash_table[food][0] = newRating
        heapq.heappush(self.cuisine_hash_table[self.food_hash_table[food][1]],[- newRating, food])

    def highestRated(self, cuisine: str) -> str:
        while self.food_hash_table[self.cuisine_hash_table[cuisine][0][1]][0] != - self.cuisine_hash_table[cuisine][0][0]:
            heapq.heappop(self.cuisine_hash_table[cuisine])
        return self.cuisine_hash_table[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end

