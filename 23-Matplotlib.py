import matplotlib.pyplot as plt
import numpy as np

valx = np.linspace(0,20,10)
valy = valx**2
plt.plot(valx,valy,"r")
plt.title("matplotlib grafiği")
plt.xlabel("X ekseni başlığı")
plt.ylabel("Y ekseni başlığı")

plt.show()


