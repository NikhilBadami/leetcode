class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        I am given a list of integers containing n+1 integers in the range [1,n]. There is exactly one repeated number in the input array and I
        need to find and return it. I cannot modify the array or use additional memory.

        One way to do this would be to reformulate the problem such that each value in the array correspond to an index in the array. Because
        I know that the input only contains numbers between 1 and n, and that there are n+1 numbers in the array, this guarantees that I will
        not go out of bounds. Treating the numbers in the array as pointers to various indicies effectively turns the list into a linked list.
        The duplicate number will form a cycle where the duplicate is the head of the cycle. I can apply Floyds algorithm to find the start of
        this cycle, which will also be the duplicate number I am trying to return

        time: O(n)
        memory: O(1)
        """
        # Since I know that the list will have at least two elements, I don't need to do any up front edge case testing.
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # Cycle found, break
                break
        
        # Find the start of the cycle
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast

