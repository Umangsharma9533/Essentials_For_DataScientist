# Import numpy as np
import numpy as np

# Set the seed, will use cerain internal calculation and come up with a solution
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Use randint() to simulate a dice
# will print any value from 1-6 , 7 wont be included in the output
print(np.random.randint(1,7))
# Use randint() again
print(np.random.randint(1,7))
#====================================================
step = 50

# Roll the dice
dice=np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice>2 and dice<=5 :
    step=step+1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

#=====================================================================
random_walk=[]
random_walk.append(0)
# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step=random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice>0 and dice <= 2:
        step = step - 1
    elif dice>2 and dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
