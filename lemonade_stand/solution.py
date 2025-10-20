class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Can use a hashmap to track how many of each bill type we have. Also, for each transaction,
        use a tracker variable change to track how much change a customer is owed. For each
        customer, we deterimine the change they need, and then traverse through a decision tree.
        At each decision point, we see what is the largest bill we can take to decrease their
        change value to 0. We follow this path until we are able to create net zero change,
        or, back track if we are unable to create the change. For each decision, we decrement
        the number of bills we have of the type we choose. We try every available bill at each
        decision. We return a bill type if it is part of the solution or an empty array if we
        cannot create a solution.

        time: 
        - O(b) to iterate through each customer
        - O(c) to iterate through the number of bills the stand owner has to make change
        - overall: O(bc)

        memory: O(c) to store the number of bills the stand owner has, O(b) in the worst case
        """
        # Create an empty map with the possible bills types
        change_map = {
            5: 0,
            10: 0,
            20: 0
        }
        # Apparently this lemonade is that good
        cost = 5

        for b in bills:
            remaining_change = b - cost
            if remaining_change != 0:
                # The customer is owed change
                can_create_change, change_map = self.createChange(change_map, remaining_change)
                if not can_create_change:
                    return False
            change_map[b] += 1
        return True
    
    def createChange(self, change_map: dict[int, int], remaining_change: int):
        """
        Helper function to determine change. Using the remaining_change variable as a guide,
        iterates through the change map and takes the most expensive bill available first
        that is less than the remaining change and selects that bill to be part of the change
        dispersed. Returns a bool if change can be created or not along with the updated change
        map.
        """
        # Possible bills
        bills = [20, 10, 5]
        for b in bills:
            # Check to see if change can be made from bill and if we have any bills of that type
            if b <= remaining_change and change_map[b] != 0:
                remaining_change -= b
                change_map[b] -= 1
                if remaining_change == 0:
                    return True, change_map
                else:
                    can_create_change, new_change_map = self.createChange(change_map, remaining_change)
                    if can_create_change:
                        return True, new_change_map
                # If we get here, no solution was found for this bill. Reset variables
                remaining_change += b
                change_map[b] += 1
        # If no bills can satisfy the change requirement, return an empty array
        return False, change_map
        
