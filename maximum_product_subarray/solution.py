class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        I'm given an integer array and I need to find the subarray that has be maximum product. A subarray is a continuous subset of elements
        within the larger array.

        How to approach this problem? What would be the solution to an array with just one number? It would be just that number. What about
        if the array contains two positive numbers? The solution would be the product of those two numbers. What about if the array contained n
        positive numbers? The solution would be the product of all of those numbers. What if there are negatives or 0's in the array? An array 
        with two elements where one is positive has answer of the positive element, same if the array has a zero and a positive element. If the 
        array has a zero and a negative element, the answer is 0.

        What if the recurrence is the question, "what is the largest product of the array up to and including the current element?". Example:
        [-3,2]. The first product would be -3, followed by -6. Since multiplying the second element by the first produces a more negative
        number, the answer is still the first product, namely -3. However, I cannot use this answer going forward since adding future elements
        to this running product would break the requirement that they be part of the same sub-array, i.e., the elements would not be
        contiguous.

        What if I modify the recurrence to be, what is the largest product I can form either adding the current element to the previous
        product, or starting a new product with the current element? I can use a single variable to track the largest running product
        and a global variable to track the largest overall product.

        time: O(n)
        memory: O(1)
        """
        best_prod = nums[0]
        cur_prod = nums[0]
        for i in range(1, len(nums)):
            if nums[i] * cur_prod < nums[i]:
                cur_prod = nums[i]
            else:
                cur_prod *= nums[i]
            best_prod = max(best_prod, cur_prod)
        return best_prod

