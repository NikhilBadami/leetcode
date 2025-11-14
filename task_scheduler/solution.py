class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        I need to output the number of cpu cycles it would take to run all tasks, subject to the constraint that tasks
        of the same letter can only be run once every n times. One way I could do this is with a priority queue. For each
        unique task, I track the next available cpu cycle for that task and add it to the queue. As I iterate through
        my cpu cycles, I pop off tasks from the queue that have a cycle availablity less than or equal to the current
        cycle. If there are no available tasks, idle the cpu. Use a map to map tasks to their next available cpu cycle

        time: O(tlog(t)) to build priority queue as well as process the queue
        memory: O(t) --> t is the number of tasks
        """
        # Build priority queue
        next_cycle = {}
        q = []
        for t in tasks:
            if t in next_cycle.keys():
                q.append((next_cycle[t], t))
                next_cycle[t] = next_cycle[t] + n + 1
            else:
                q.append((1, t))
                next_cycle[t] = 1 + n + 1
        
        import heapq
        heapq.heapify(q)

        # Process queue to get order of tasks
        cycles = 0
        while len(q) > 0:
            cycles += 1
            if q[0][0] <= cycles:
                heapq.heappop(q)
        return cycles

        
