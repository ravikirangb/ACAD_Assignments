# Author: Ravikiran Bailkeri

# Assignment 2 Python- 1 session :Write a program which will find all such numbers which are divisible by 7 but are not a
#   multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be
#   printed in a comma-separated sequence on a single line.

import sys, os

# For loop 
# If condition for checking 
for n in range(2000, 3200):
     if (n%7 == 0) and (n%5 != 0):
         print(n, "is Divisible by 7 but not a multiple of 5")
         
