import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
 
# Initializing the random seed
rand_seed=1000
 # covariance values
cov_val = [-0.4, 0, 0.4]
 
mean = np.array([0,0])
 
# Iterating over different covariance values
for idx, val in enumerate(cov_val):
    plt.subplot(1,3,idx+1)
     
    # Initializing the covariance matrix
    cov = np.array([[1, val], [val, 1]])
     
    # Generating a Gaussian bivariate distibution with given mean and covariance matrix
    dist = multivariate_normal(cov = cov, mean = mean,
                                seed = rand_seed)
     
    # Generating 5000 samples out of the distibution
    x = dist.rvs(size = 5000)
     
    # Plotting the generated samples
    plt.plot(x[:,0],x[:,1], 'o', c='red',
             markeredgewidth = 0.5,
             markeredgecolor = 'black')
    plt.title(f'Covariance between x1 and x2 = {val}')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.axis('equal')
     
plt.show()