import seaborn as sns
import matplotlib.pyplot as plt

veriler = sns.load_dataset("exercise")

g = sns.displot(data=veriler, x="pulse")

g.figure.suptitle("Pulse Distribution")
g.figure.canvas.manager.set_window_title("Displot")

plt.show()