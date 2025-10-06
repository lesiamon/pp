import numpy as np
import matplotlib.pyplot as plt
# Data
x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

# Parameters
w, b = 0.0, 0.0
lr = 0.1
losses = []

# Training loop
for i in range(10):
    y_pred = w * x + b
    loss = np.mean((y - y_pred)**2)
    dw = -2 * np.mean(x * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    w -= lr * dw
    b -= lr * db
    losses.append(loss)
    
    #plot losses
    plt.plot(losses)
    plt.xlabel('Iteration')
    plt.ylabel('Loss') 
    plt.title('Loss over Iterations')
    plt.show()