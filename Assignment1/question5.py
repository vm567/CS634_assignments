import numpy as np
import matplotlib.pyplot as plt
# Arrival rates of the API requests
A= [1, 3, 4]
# Service time of the requests (exponential random variable with rate 4)
service_time = np.random.exponential(scale=1/4, size=10000)
#Time units
T = 100
#Step size
dt= 0.005
# Number of time steps
n_steps = int(T / dt)
# Initialize the number of requests waiting in the queue
queue_length = np.zeros((len(A), n_steps))
# Simulate the behavior of the queue for i,
print(n_steps)
print(len(service_time))
for i, a in enumerate(A):
    time = 0
    requests = 0
    for j in range(len(service_time)):
        if np.random.rand() < a * dt:
            requests += 1
        if requests >0:
            time += dt
            service = service_time[j]
            if time >= service:
                time -=service
                requests -= 1
                queue_length[i, j] = requests
# Plot the number of requests waiting in the queue as a function of timetime = np.arange(0, T, dt)

print(queue_length)
time = np.arange(0, T, dt)

for i, a in enumerate(A):
    print("what is a",a) 
    print("what is i",i) 
    plt.plot(time, queue_length[i, :], label='Arrival rate = {}'.format(a))
    plt.xlabel('Time')
    plt.show()