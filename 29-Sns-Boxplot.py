import seaborn as sns
import matplotlib.pyplot as plt

veriler = sns.load_dataset("exercise")

plt.figure("Boxplot")

sns.boxplot(
    x="time",
    y="pulse",
    data=veriler
)

plt.title("Pulse by Time")
plt.show()