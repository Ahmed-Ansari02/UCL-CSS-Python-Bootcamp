import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = [2*x for x in x]
# Create a figure and two subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))

# Plot the first function
ax1.plot(x, y1)
ax1.set_title('Sine Wave')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# Plot the second function
ax2.plot(x, y2)
ax2.set_title('Cosine Wave')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

ax3.plot(x, y3)
ax3.set_title('Linear Function')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
# Adjust spacing and display the plot
plt.subplots_adjust(hspace=0.5)
plt.show()