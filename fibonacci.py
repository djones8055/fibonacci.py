""" fibonacci program, enter how many steps you want to take and
    the program will show you the sequence that many steps deep"""

NUM = int(input("How many steps do you want to take? "))
STEPS = 0

NUM1 = 0
NUM2 = 1

while STEPS < NUM:
    NEWNUM = NUM1 + NUM2
    NUM1 = NUM2
    NUM2 = NEWNUM
    print(NEWNUM)
    STEPS = STEPS + 1
