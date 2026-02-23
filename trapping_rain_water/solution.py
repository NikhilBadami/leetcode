class Solution:
    def trap(self, height: List[int]) -> int:
        """
        I'm given an array, height, that contains the elevation map for a certain terrain. I need to determine how much water would
        be trapped in this region.

        The amount of water that can be trapped is dependent on the topology of the region. In order for water to be trapped, there
        needs to be a wall on each side to hold the water. The amount of water that can be stored is dependent on the shorter wall.
        I.e., if there are two walls, one of height 1 and one of height 2, only water to height 1 can be trapped. One thing to note
        is that each wall has a width of 1, so water can be stacked on top, as opposed to if the walls had no volume.

        I need a way to track topology as well as the bounds of the container. One thing I can do is to track each spot in the
        terrain using a stack. When I encounter a tile with a height greater than the top of the stack, I pop this value from the stack.
        Note that this is not the left wall of the container but the **bottom** of the container. In other words, if there is elevation
        in the region, I want to account for it. The bounds of the container will be the current right pointer and the new top of the
        stack, which serves as the left pointer. Crucially, I also do not want to try and calculate the area for the entire container
        as there may be differing levels of elevation within the container. To account for this, I track the amount of water that can
        be trapped assuming the walls were right next to the curren tile. I then add up each result I find into a global result. One
        last thing to note is that since I am using a stack, I should pop every tile that can be solved with the current right pointer.

        time: O(n)
        memory: O(n)
        """
        res = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                b = height[stack.pop()]
                if stack:
                    r = height[i]
                    l = height[stack[-1]]
                    h = min(r, l) - b
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res

        
