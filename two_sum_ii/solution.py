class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Since the problem is asking to use only constant memory, I can use two pointers to solve the problem. I initialize
        a pointer at the start and end of the array and add the numbers at these pointers. If the sum is too large, I
        decrement the right pointer. If it is too small, I increment the left pointer. Continue doing this until the
        solution is found.

        time: O(n)
        memory: O(1)
        """
        l, r = 0, len(numbers) - 1

        res = None
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                res = [l+1, r+1]
                break
        return res
        
