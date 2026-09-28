import seaborn as sns
import matplotlib.pyplot as plt

veriler = sns.load_dataset("exercise")

g = sns.pairplot(veriler)

g.figure.suptitle("Exercise Dataset Pairplot", y=1.02)
g.figure.canvas.manager.set_window_title("Pairplot")

plt.show()
