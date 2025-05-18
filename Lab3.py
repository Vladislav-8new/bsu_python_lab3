import matplotlib.pyplot as plt
import statsmodels.api as sm

iris = sm.datasets.get_rdataset("iris", "datasets").data

colors = {'setosa': 'purple', 'versicolor': 'teal', 'virginica': 'gold'}

plt.figure(figsize=(8, 6))
for species, color in colors.items():
    subset = iris[iris['Species'] == species]
    plt.scatter(
        subset['Petal.Length'],
        subset['Petal.Width'],
        label=species,
        color=color
    )

plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.title("Iris' petal sizes")
plt.legend()
plt.grid(True)
plt.show()
