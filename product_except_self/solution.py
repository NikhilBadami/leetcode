class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        To solve this problem without division, I need to use a prefix and postfix array. The prefix array's elements will
        be the product of each element up to i not including i and the postfix will be the product of every element
        starting at the end of the array excluding i. The result will the prefix[i-1] * postfix[i+1]

        time: O(n)
        memory: O(n)
        """
        from collections import deque
        prefix = [1]
        postfix = deque()
        postfix.append(1)

        # Create prefix
        for i in range(len(nums)):
            prefix.append(prefix[i] * nums[i])
        # Create postfix
        for i in range(len(nums)-1, -1, -1):
            postfix.appendleft(postfix[0] * nums[i])
        
        # Create result
        res = []
        prefix_ctr = 1
        for i in range(len(nums)):
            res.append(prefix[prefix_ctr-1] * postfix[i+1])
            prefix_ctr += 1
        return res
        
