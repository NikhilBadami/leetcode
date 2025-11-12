class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        The parameter I'm searching for is k, the minimum speed koko can eat at such that she can eat all the bananas
        within h hours. The restrictions are, all bananas must be eaten within h hours. Koko will eat at a rate of k
        bananas per hour, but if she encounters a pile with less than k bananas, she will eat that whole pile only.

        One way to do this would be to test different values of k starting at 1 and then iterating through the piles
        list to check how quickly the bananas could be eaten at this rate k. For each hour, I would decrement the current
        pile by k, or exhaust it if the number of bananas remaining is less than k and then move on to the next pile on the
        next hour. If I can exhaust every pile before h has completed, this is a valid value for k.

        However, I need to return the minimum value of k. Again, I could start iterating from 1, but this could be
        inefficient if the true k value is very large. If I consider all possible values of k as a sorted array, I
        could use binary search to find it. What would the bounds of the search be? Given a list of piles, what is the
        most amount of bananas koko can eat in an hour that would make sense? It would the the largest pile, since koko
        will never eat more bananas than there are in a pile, the largest pile is the upper bound for the search. So the
        bounds are 1 <= k <= max(piles)

        What are the exit conditions? Normally in binary search you search for a target value. What is my target value in
        this search? Maybe there is no specific target, rather the exit condition is based on how quickly koko can eat
        at the given rate k. For a given rate k, if she can eat the bananas in less than h hours, we need to find a smaller
        value of k. If she can't eat all the bananas in h hours, we need to find a larger value of k. The search ends when
        we find a value of k such that koko eats all the bananas in exactly h hours

        time: to find k: O(log(b)) where b is the largest pile in piles
              to test a given value of k: O(h) where h is the number of hours
              to find max in piles: O(p) where p is the number of piles
              overall: O(hlog(b) + p)
        memory: O(1)

        *********************************
        Keeping the above in tact for future reference but, the search conditions ended up being dependent on the hours.
        If after eating all piles, it took koko longer than h hours at a particular k, we knew to search for values 
        greater than the current k. If she ate quickly enough, i.e., hr < h, then this is a valid value of k. However, we
        are not interested in the first valid value of k we find, instead, we want the fastest k she can eat in. So if
        we find a valid value, we keep searching.
        """
        import math
        l, r = 1, max(piles)

        # Search for the optimal value of k.
        while l <= r:
            k = l + (r - l) // 2
            # Test if this value of k can eat all the bananas in exactly h hours
            # Counter for piles
            p = 0
            # Counter for hours
            hr = 0
            while p < len(piles):
                pile = piles[p]
                # Determine number of hours it takes to eat pile
                hr += math.ceil(pile / k)
                p += 1
            if hr > h:
                # This k is too slow
                l = k + 1
            else:
                # This k is valid, but there could be a better one
                r = k - 1
        return l


        
