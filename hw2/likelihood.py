import matplotlib.pyplot as plt
import numpy as np

thetas = np.linspace(0, 1, 100)

def bernoulli_likelihood(thetas, n, i):
    return thetas**i * (1 - thetas)**(n - i)

plt.plot(thetas, bernoulli_likelihood(thetas, 10, 6))
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L(\theta)$')
plt.show()

plt.plot(thetas, bernoulli_likelihood(thetas, 5, 3))
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L(\theta)$')
plt.show()

plt.plot(thetas, bernoulli_likelihood(thetas, 100, 60))
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L(\theta)$')
plt.show()

plt.plot(thetas, bernoulli_likelihood(thetas, 10, 5))
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L(\theta)$')
plt.show()
