import seaborn as sns
import matplotlib.pyplot as plt

veriler = sns.load_dataset("exercise")
print(veriler.head())

sns.displot(data=veriler, x="pulse")
plt.title("Displot Grafiği")
plt.show()

sns.pairplot(veriler)
plt.title("Pairplot Grafiği")
plt.show()

sns.boxplot(x="time", y="pulse", data=veriler)
plt.title("boxpolot Grafiği")
plt.show()