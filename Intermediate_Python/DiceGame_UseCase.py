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
# Numpy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
