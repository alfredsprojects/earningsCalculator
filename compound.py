

import math
import random



capital = 1000
weeks = 0
capitalGoal = 100000
percent = .15

while capital <= capitalGoal:
    weeks += 1
    capital = capital + (capital*percent)

print("Capital %d ; Weeks %d" % (capital, weeks))