import matplotlib.pyplot as plt
import numpy as np

vala = np.linspace(0,20,100)
valb = vala**2

plt.subplot(1,2,1)
plt.plot(vala,valb,"b")
plt.title("y = x^2")

plt.subplot(1,2,2)
plt.plot(valb,vala,"r")
plt.title("eksenler ters")

plt.show()


