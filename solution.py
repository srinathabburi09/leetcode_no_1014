class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_i = values[0] + 0    #values[i] + i this is the initialzation of values[i] + i
        max_score = float("-inf")    # to evaluate the max_score we initialize it to negetive infinity

        for j in range(1, len(values)):      #iterating j over the loop expect at index 0
            max_score = max(max_score, max_i + values[j] - j)  #to get better max_score we get max among previous max_score and max_i + values[j] - j as per the question
            max_i = max(max_i, values[j] + j)  #why we mentioned values[j] + j this is because we need to get the future i values into it.To get the future values i and to reduce complexity we get by adding and taking better max sum among those 2.

        return max_score   #finally we return max_score after keeps updating

#time complexity - O(n) - interating j over the loop 
#space complexity - O(1) - no extra space because we arnt storing any thing
      
