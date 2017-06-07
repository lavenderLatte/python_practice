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

"""
[My Problem]
When I run the code below in Python2, it prints 'succeeded: 5.0'. Whereas when I run it in Python3, it prints 'succeeded: 4.999999999999998'.
Why is it different in those two?
And how come Python3 can get answer like 4.999999999999998 when I increment by 0.1 only?
"""

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2 - x) >= epsilon: 
    if guess <= x:  
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))