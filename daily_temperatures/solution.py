class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        For each array element, need to find how many days it will take until a larger element appears. In other words,
        if arr[0] == 5 and arr[2] == 7 (with arr[1] == 0) then answer[0] = 2 because it will take two days for there to be
        an array element with a higher value.

        The brute force solution would be to do a linear scan of the array, i.e., starting at each element, iterate until
        an elment with a larger value is found. This would take worst case O(n^2) time.

        When encountering an element, it can act as the solution for multiple preceeding elements. So, I can check
        multiple previous entries to see if they are "solved" by this current entry. This suggests I can use a stack
        to solve the problem,  in other words, as I iterate through the array, store each element on the stack. At the
        next element, I pop of from the stack each element that is solved by this current element, i.e., cur > past.
        I'll need to stack each element as a tuple with its value and index in the array so I can update the answer.

        time: O(n)
        memory: O(n)
        """
        from collections import deque
        q = deque()
        answers = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(q) == 0:
                # Store tuple of (value, index)
                q.appendleft((temperatures[i], i))
            else:
                while len(q) > 0 and temperatures[i] > q[0][0]:
                    top_el = q.popleft()
                    answers[top_el[1]] = i - top_el[1]
                q.appendleft((temperatures[i], i))
        return answers
        
