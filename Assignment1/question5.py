import numpy as np
import matplotlib.pyplot as plot
A= [1, 3, 4]
T = 100
serv_time = np.random.exponential(scale=1/8, size=5000)

t= 0.008
n_steps = int(T / t)
# Initialize the number of requests in the queue
queue_length = np.zeros((len(A), n_steps))
print(n_steps)
print(len(serv_time))
for i, a in enumerate(A):
    time = 0
    requests = 0
    for j in range(len(serv_time)):
        if np.random.rand() < a * t:
            requests += 1
        if requests >0:
            time += t
            service = serv_time[j]
            if time >= service:
                time -=service
                requests -= 1
                queue_length[i, j] = requests

print(queue_length)
time = np.arange(0, T, t)
for i, a in enumerate(A):
    plot.plot(time, queue_length[i, :], label='Arrival rate = {}'.format(a))
    plot.xlabel('Time')
    plot.show()cd