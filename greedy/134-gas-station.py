class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_sum = 0
        total_sum = 0
        last_negative = 0
        ### initially at first stop we fill it out up with no cost 
        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]
            current_sum += gas[i]
            current_sum -= cost[i]
            if current_sum < 0:
                last_negative = i+1
                current_sum = 0
        
        
        return last_negative if total_sum >= 0 else -1
            