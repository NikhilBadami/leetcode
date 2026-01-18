class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Straight forward approach would be to process the array into a set and then iterate the range [1,n] and find the duplicate like that but
        this requires using O(n) extra space and the problem requires using O(1) extra space. A naive way would be to process each array element
        individuall, i.e., for each element, check every other subsequent element to see if there is a duplicate (O(n^2)). Assuming sorting doesn't
        count as modifying the array, I can sort the array and then make a single pass checking if the current element equals the element before 
        it (O(nlog(n))). Both solutions have O(1) extra memory.    
        """
        # O(nlog(n)) solution
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        return -1
        
