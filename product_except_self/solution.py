class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        The ask is to return an array where arr[i] is the product of all elements in the input array nums except for 
        nums[i]. The naive approach is to get the product of the entire array and then loop through nums, dividing out
        nums[i] from the solution. The edge case is if there is a 0 present in the array, as dividing by 0 is undefined.
        If there is a single 0, then I can ignore that 0 and find the product of the rest of the elements of nums. This
        will be the answer for nums[i] == 0. If there is more than 1 0, then the solution is 0 for every element.

        time: O(n)
        memory: O(n)
        """
        # Base case for product
        prod = 1
        # Records solution for case where there is a single 0
        single_zero_found = False

        # Find nums product
        for n in nums:
            if n == 0:
                if not single_zero_found:
                    single_zero_found = True
                else:
                    prod = 0
            else:
                prod *= n
        
        # Build solution
        res = []
        for n in nums:
            if single_zero_found:
                if n == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // n)
        return res
