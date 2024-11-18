import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20) 
y1 = 2 * x + 5 
y2 = 4 * x  

plt.subplot(2, 1, 1)  
plt.plot(x, y1, 'bo-', label='y = 2x + 5') 
plt.legend()

plt.subplot(2, 1, 2) 
plt.plot(x, y2, 'rs--', label='y = 4x')  
plt.legend()

plt.tight_layout()  
plt.show() 