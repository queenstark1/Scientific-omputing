
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Concurrent users and measured server response time (milliseconds)
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

# A simple quadratic model for increasing delay
def model(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the model to the measured data
parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters

# Calculate predictions and the root mean square error
predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 450 users: {model(450, a, b, c):.2f} ms")

# Plot measured data and fitted curve
x_plot = np.linspace(users.min(), 450, 300)

plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the graph
plt.savefig("plots/Task_14_curve_fitting.png", dpi=150)
print("Graph saved to plots/Task_14_curve_fitting.png")
