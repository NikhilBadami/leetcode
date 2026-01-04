class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        I need to find the minimum number of jumps needed to reach the end of the array starting at index 0. Each element in the input
        nums represents the maximum jump I can make at that point, though I am able to make smaller jumps if necessary.

        I can approach this problem as follows. I allocate another array of size nums that represents the minimum number of steps it
        takes to reach the end from that point. The base case will be 0, which will be the final entry in the array. Then, I iterate
        backwards through nums to find how many steps from each point it will take to reach the end. If I can reach the end in 1
        step, this is the minimum possible number of steps and I record this value immediately. If it takes more than 1 step, I
        iterate through the possible number of steps from this point and keep the best value. Specifically, I make the largest
        possible jump first, then iterate backwards, keeping the minimum number of steps it will take to reach the end. I return
        the value in the first index of the new array. Note it is possible to have no jumps available at a given spot, in which case
        this spot can never reach the end and its value in the new array is 0.

        time: O(n^2)
        memory: O(n)
        """
        num_steps = [0] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue
            # Check if the spot can reach the end directly
            if i + nums[i] >= len(nums) - 1:
                num_steps[i] = 1
                continue
            # Loop through the possible number of jumps, starting with the largest. Keep the minimum value
            num_jumps = 10001  # Max length is 10000
            for j in range(nums[i], 0, -1):
                # Skip values that are 0 or that would exceed the length of the array
                if num_steps[i+j] == 0:
                    continue
                num_jumps = min(num_jumps, 1 + num_steps[i+j])
            num_steps[i] = 0 if num_jumps == 10001 else num_jumps
        return num_steps[0]
