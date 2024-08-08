#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        hash_table = {"1": ["One"], 
                      "2": ["Two", "Twenty"],
                      "3": ["Three", "Thirty"], 
                      "4": ["Four", "Forty"], 
                      "5": ["Five", "Fifty"],
                      "6": ["Six", "Sixty"],
                      "7": ["Seven", "Seventy"],
                      "8": ["Eight", "Eighty"],
                      "9": ["Nine", "Ninety"],
                      "10": ["Ten"],
                      "11": ["Eleven"],
                      "12": ["Twelve"],
                      "13": ["Thirteen"],
                      "14": ["Fourteen"],
                      "15": ["Fifteen"],
                      "16": ["Sixteen"],
                      "17": ["Seventeen"],
                      "18": ["Eighteen"],
                      "19": ["Nineteen"]}
        if num == 0:
            return "Zero"
        else:
            number_list = []
            while num > 0:
                number_list.insert(0, num % 10)
                num //= 10
            result = ""
            counter = 0
            while number_list:
                triplets = []
                index = len(number_list) - 1
                while index >= 0 and len(triplets) < 3:
                    triplets.insert(0, number_list[index])
                    number_list.pop()
                    index -= 1
                while len(triplets) < 3:
                    triplets.insert(0,0)
                string = ""
                for i, c in enumerate(triplets):
                    if i == 0 and c != 0:
                        string += hash_table[str(c)][0]
                        string += " Hundred"
                    elif i == 1:
                        if c == 1:
                            if string == "":
                                string += hash_table[str(c)+str(triplets[i + 1])][0]
                            else:
                                string += " " + hash_table[str(c)+str(triplets[i + 1])][0]
                        elif c > 1:
                            if string == "":
                                string += hash_table[str(c)][1]
                            else:
                                string += " " + hash_table[str(c)][1]
                    elif i == 2 and triplets[1] != 1 and c != 0:
                        if string == "":
                            string += hash_table[str(c)][0]                     
                        else:
                            string += " " + hash_table[str(c)][0]

                if counter == 0 and string != "":
                    result = string + result
                elif counter == 1 and string != "":
                    if result == "":
                        result = string + " Thousand" + result
                    else:
                        result = string + " Thousand " + result
                elif counter == 2 and string != "":
                    if result == "":
                        result = string + " Million" + result
                    else:
                        result = string + " Million " + result
                elif counter == 3 and string != "":
                    if result == "":
                        result = string + " Billion" + result
                    else:
                        result = string + " Billion " + result
                counter += 1
            return result
# @lc code=end

