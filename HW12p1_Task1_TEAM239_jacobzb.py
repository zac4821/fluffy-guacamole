# Activity: Homework 12.1
# File: HW12_p1_Task1_TEAM239_jacobzb
# Date:      21 November 2019
# By:        Zac Jacob
# Section:   019
# Team:      239

# ELECTRONIC SIGNATURE
# Zachary Jacob

# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES

import math

while True:
    a = input('Would you like the desired angle to be in radians [0] or degrees [1]?\n')
    if a == '0':
        b = '2pi'
        break
    elif a == '1':
        b = '360 degrees'
        break
    else:
        print('Unknown Command')

while True:
    a = float(input('Please enter angle between 0 - {0}: '.format(b)))
    if b == '2pi' and 0 < a < 2 * math.pi:
        break
    elif b == '360 degrees' and 0 < a < 360:
        a = a * math.pi / 180
        break
    else:
        print('\nAngle entered outside accepted range.\nPlease try again.\n')

n = float(input('Please enter desired number of terms for Taylor Series: '))

def term(a, n):
    c = 0
    for i in range(n):
        c += (-1) ** i * (a ** (2 * i)) / math.factorial(2 * i)

print(c)



