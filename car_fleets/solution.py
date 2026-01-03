class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        I'm given a target, a set of starting positions and a set of speeds. The position input represents the starting position of
        each car and speed represents how fast each car is moving. I need to determine how many car fleets reach the target. A car
        fleet is a group of cars all moving at the same speed. Initially, each car is its own fleet. Because cars cannot pass each
        other, if a faster car catches up to a slower car, it now travels alongside the slower car at the pace of the slower car and
        the two form their own fleet.

        One way to solve this would be to simulate each time step, i.e., iterate over the input and add the speed of each car to its
        current position to get its next position. This would be inefficient and would have time complexity approaching O(n^2).
        Instead, I can do the following:

        1: Sort the input. The position input gives the starting position of each car, but the positions are not ordered in the
        actual ordering of the cars. For example, if the input was [5,1,4], on an actual road the 0th car would be the farthest,
        the 1st car would be the farthest back and the last car would be in the middle. Sorting makes it so that the index of
        each position reflects where the car is on the road.

        2. To solve this in one pass, I only need to determine how long it will take each car to reach the target from its current
        position at its given speed. I can calculate the time it will take a car to reach the target as (target - pos) / speed. I can
        store each time in the same index as the car it corresponds to. Then, I iterate from the back of the array. I do this because
        the car farthest ahead will act as the "limiter" if any cars catch up to it. As I iterate backwards, I record the time of
        the farthest forward car as the initial limiter. Any car that has a time less than the current car is added to the fleet
        of the current car. This is because if a car behind the farthest back car would reach the target before this car, we know
        that at some point it would need to pass the current car. We know this isn't allowed in the context of the problem, so these
        cars would form a car fleet. When I encounter a time greater than the current time, this becomes the new limiter.

        time: O(nlog(n)) --> Limited by initial sort
        memory: O(n) --> Need to pre-process input into tuples and store speeds
        """
        # Process inputs into arrays of [position, speed] and sort by position
        car_info = []
        for i in range(len(speed)):
            car_info.append([position[i], speed[i]])
        car_info.sort(key=lambda x: x[0])

        # For the sorted list, calculate the time it would take for each car to reach the target
        # Initialize to time it would take car farthest along to reach target
        farthest_car = car_info[-1]
        limiting_time = (target - farthest_car[0]) / farthest_car[1]
        # n is at least 1 so there is at least 1 fleet for any input
        fleets = 1
        for i in range(len(car_info)-1, -1, -1):
            # Calculate the time of the current car
            cur_car = car_info[i]
            cur_time = (target - cur_car[0]) / cur_car[1]
            # If the current time is greater than the time of the current limiter, update the limiting time
            # This is because a slower time means this car will never reach the current limiting car and thus will never join its
            # fleet
            if cur_time > limiting_time:
                limiting_time = cur_time
                # This means a new fleet is formed
                fleets += 1
        return fleets
        
