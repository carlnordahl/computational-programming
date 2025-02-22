import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1e-6, 100, 1000)

appr_sqrt = lambda x, x_prev: (x_prev + x/x_prev)/2

def approximate_root_many(x, n):
    # iterate approximation n times
    # if n = -1 make many approximations until they converge
    # convergence criteria: |x_k - x_k-1| < 10^-6

    x_prev = x/2

    if n == -1:
        conv = False
        while not conv:
            x_next = appr_sqrt(x, x_prev)
            if np.abs(x_next - x_prev) < 1e-6:
                conv = True
            x_prev = x_next
    
    else:
        for i in range(n):
            x_next = appr_sqrt(x, x_prev)
            if np.abs(x_next - x_prev) < 1e-6:
                conv = True
            x_prev = x_next
    
    return x_prev

# y_ref : reference
y_ref = np.sqrt(x)

# y_m : many iterations
y_m = np.linspace(0, 0, num=0)

for v in x:
    y_m = np.append(y_m, approximate_root_many(float(v), -1))

# y_1 : one iteration
y_1 = np.linspace(0, 0, num=0)

for v in x:
    y_1 = np.append(y_1, approximate_root_many(float(v), 1))

# y_2 : two iterations
y_2 = np.linspace(0, 0, num=0)

for v in x:
    y_2 = np.append(y_2, approximate_root_many(float(v), 2))

# y_3 : three iterations
y_3 = np.linspace(0, 0, num=0)

for v in x:
    y_3 = np.append(y_3, approximate_root_many(float(v), 3))

# y_4 : four iterations
y_4 = np.linspace(0, 0, num=0)

for v in x:
    y_4 = np.append(y_4, approximate_root_many(float(v), 4))


plt.plot(x, y_m, linestyle='dotted')
plt.plot(x, y_1, color='red')
plt.plot(x, y_2, color='orange')
plt.plot(x, y_3, color='green')
plt.plot(x, y_4, color='blue')

plt.legend(['many', '1', '2', '3', '4'])
plt.title('Approximation of square-root function')
plt.show()

plt.savefig('root-approximation')