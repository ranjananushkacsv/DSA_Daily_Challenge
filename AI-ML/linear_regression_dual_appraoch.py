'''
Implementing linear regression in two ways - first via normal equation with L2 ridge
and the other by using gradient descent.
The requirement is - 
1. We have to implement this by using numpy only
2. we have to show the graph of the loss curve
'''

import numpy as np
import matplotlib.pyplot as plt

#fake data
np.random.seed(0)
n_samples = 200
#we are considering 2 features
x_raw = np.random.randn(n_samples,2)
true_w = np.array([3.0,-0.2])
true_b = 4.0
y = x_raw@ true_w +true_b + 1.0 * np.random.randn(n_samples)

#adding bias 

x = np.hstack([np.ones((n_samples,1)), x_raw])

lam = 0.01

#loss func = mse + l2 penalty, we don't penalize the bias term
def loss(w):
    error = x @ w - y 
    mse = np.mean(error**2)
    penalty = lam * np.sum(w[1:]**2)
    return mse+penalty

# normal method - Closed form
def solve_closed_form():
    n_features = x.shape[1]
    I = np.eye(n_features)
    I[0,0]=0

    A = x.T@ x +n_samples * lam * I
    b = x.T @ y
    return np.linalg.solve(A,b)

def gradient(learning_rate=0.1, n_iterations=3000):
    w = np..zeros(x.shapes[1])
    history = []
    
    for _  in range(n_iterations):
        error = x@ w- y
        grad = (2/ n_samples) * (x.T @ error)
        grad[1:] += 2 * lam * w[1:]

        w = w - learning_rate * grad
        history.append(loss(w))

    return w, history 

# comparing and running both approaches

w_closed = solve_closed_form()
w_gd, history = gradient()

print("Closed form weights [b, w1, w2]:", np.round(w_closed, 4))
print("Gradient descent     [b, w1, w2]:", np.round(w_gd, 4))
print("Do they match? ", np.allclose(w_closed, w_gd, atol=1e-2))


# matplotlib for graphical representation of gradient descent loss curve
plt.figure(figsize=(7, 4))
plt.plot(history)
plt.xlabel("Iteration")
plt.ylabel("Loss (MSE + ridge)")
plt.title("Gradient descent loss curve")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("loss_curve.png", dpi=120)
print("Saved loss curve to loss_curve.png")