# technest_finger exercise pg.30?
"""
[Question]
Write a program that asks the user to enter an integer and prints two integers, 'root' and 'pwr',
such that 0 < pwr < 6 and root ** pwr is equal to the integer entered by user.
If no such pair of integers exists, it should print a message to that effect.

[My Problem]
My code below works for positive integer but not for negative one.
"""

root = 0 
user_input = int(input("enter an integer:"))

for pwr in range(1, 6): 
    """
    Since power is only limited to [1, 2, 3, 4, 5], even if the input is really large number, 
    This code only will calculate three times. 
    """
    root = user_input ** (1/pwr)
    print("pwr:", pwr, ", possible_root:", root)
    
    if int(root) ** pwr == user_input:
        print("For your input the root is (", int(root), ") and pwr  is (", pwr, ")")