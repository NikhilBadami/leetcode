class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        I'm given several bits of information. I have several car positions in the position array and each of those cars are going
        at a speed given in the speed array, i.e., the car at position[i] is going at speed[i]. I need to determine how many
        car fleets arrive at target. A car fleet is a group of cars travelling at a certain speed. Cars start out independently
        but if at any point they arrive at the same position during iteration, including at the target position, the group is
        considered a fleet and moves at the speed of the slowest car in the fleet.

        I can iterate until every car reaches the target. How will I know when each car has reached the target? When each value
        in the position array is >= target. On each iteration, I update the position of each car based on its speed. If at any point
        the position of any number of cars are equal, I combine them into a single fleet and change their speed to the speed of the
        slowest car in the fleet.

        How can I represent a fleet? On each iteration, I make a pass over position to update each position based on speed. Then,
        I make a second pass to check if any values in position are equal to each other. I can hash the values of position to
        the slowest speed of any car at that position. Then, I update the position array based on the map, i.e., I re-create position
        and speed based on the map where a fleet of cars are combined into a single position in position and have a speed given by
        the slowest car in the fleet. Additionally, for any car/fleet whose position is greater than or equal to the target, I
        remove it from position and increment the counter. Note that this check should happen after I combine cars into fleets.

        time: O(n) --> Multiple single passes over the input
        memory: O(n) --> Use a map to recreate position and speed
        """
        num_fleets = 0
        while len(position) > 0:
            # Iterate over the position array and update values based on speed
            for i in range(len(position)):
                position[i] += speed[i]
            
            # Make a second pass over the array. If a car's position is <= target, hash that car's position to its speed. If
            # multiple cars are at the same position, save the slowest speed. For cars whose position is > target, add it to the
            # number of fleets that arrived at the target
            fleets = {}
            for i in range(len(position)):
                if position[i] > target:
                    position[i] = target
                if position[i] in fleets.keys():
                    fleets[position[i]] = min(fleets[position[i]], speed[i])
                else:
                    fleets[position[i]] = speed[i]
            
            # Re-create the position/speed arrays. If the position equals the target, do not add that key to the new arrays and
            # instead update the num_fleets counter
            position = []
            speed = []
            for p in fleets.keys():
                if p == target:
                    num_fleets += 1
                else:
                    position.append(p)
                    speed.append(fleets[p])
        return num_fleets

