class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Naive solution is to iterate through the gas array and check if starting from that station, can you travel clockwise around the circle. 
        This requires processing each gas stations once for every other gas station in the worst case, leading to an O(n^2) solution.

        time: O(n^2)
        memory: O(1)
        """
        for i in range(len(gas)):
            starting_station = i
            cur_gas = 0
            j = i
            # Target station is the station right before this one. Once I reach this station, I check to see if I can return to the starting
            # station. If so, I return that index. Otherwise, I continue looping
            target_station = starting_station - 1 if starting_station - 1 >= 0 else (starting_station - 1) + len(gas)
            while j != target_station:
                # Check to see if the next station can be reached
                # Fill up the tank
                cur_gas += gas[j]
                # Travel to the next station
                cur_gas -= cost[j]
                if cur_gas < 0:
                    break
                j += 1
                if j >= len(gas):
                    j = 0
            if j == target_station:
                # Final check to see if we can return to the starting stations
                cur_gas += gas[j]
                if cur_gas - cost[j] >= 0:
                    return starting_station
        
        return -1
        
