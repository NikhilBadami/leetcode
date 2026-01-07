class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Need to find the product of two non-negative numbers, meaning the numbers could be 0 or 1 or greater. I cannot convert
        the numbers into strings and I must return a string. I can use an order counter to determine how many 0s to append to the
        result of multiplying one digit by the other number, i.e., if I'm multiplying 50X11, First row would have no 0s, second row
        would have 1 at the end, if there was a third row, it would have 2 and so on.

        I don't necessarily need to do the intermediate operations as strings. Meaning, I can keep the first row of multiplication
        as ints and use a running sum. For each digit, I calculate the product by multipling the first number by that digit of
        the second number. I then multiply it by the correct order, i.e., 1, 10, 100 etc. depending on where in the multiplication
        process I am. I can then add this to the running result.

        time: O(n^2) --> n is the number of digits. I need to loop through all digits to get product
        memory: O(n) --> Will ultimately convert integer result back to string
        """
        if num1 == '0' or num2 == '0':
            # Optimization for known edge cases
            return '0'
        
        order = 0
        res = 0
        # Multiply num1 by every digit in num2 starting from the last digit. For each subsequent digit, multiply the result by order
        # which is used as 10**order
        for i in range(len(num2)-1, -1, -1):
            cur_digit = int(num2[i])
            # Define a carry if multiplication exceeds 10
            carry = 0
            cur_res = 0
            cur_order = 0
            for j in range(len(num1)-1, -1, -1):
                prod = cur_digit * int(num1[j])
                cur_res += (prod % 10 + carry) * (10 ** cur_order)
                carry = prod // 10
                cur_order += 1
            if carry > 0:
                cur_res += carry * (10 ** cur_order)
                res += cur_res * (10 ** order)
            else:
                res += cur_res * (10 ** order)
            order += 1
        return str(res)
    

