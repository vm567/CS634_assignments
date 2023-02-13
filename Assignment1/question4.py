
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Load the dataset into a pandas DataFramedf
df = pd.read_csv('data/dataset.csv',delimiter=',')
del(df['Index'])
print(df.head())


# Plot the histogram of the number of cyclists
plt.hist(df['Brooklyn Bridge'],bins=50)
plt.xlabel('Number of cyclist')
plt.ylabel('Frequency')
plt.title('Histogram of the Number of Cyclists Crossing the Brooklyn Bridge')
plt.show()


# Parameters of the Poisson distribution
lambda_ = df['Brooklyn Bridge'].mean() # mean of the observed number of cyclists
n_samp = 10000 # number of samples to generate
#Generatethe simulated number of cyclists sim_cyclists
sim_cyclists = np.random.poisson(lambda_, n_samp)
# # Plot the histogram of the simulated number of cyclists
plt.hist(sim_cyclists, bins=50)
plt.xlabel('Number of Cyclists')
plt.ylabel('Frequency')
plt.title('Histogram of the Simulated Number of Cyclists Crossing the Brooklyn Bridge')
plt.show()