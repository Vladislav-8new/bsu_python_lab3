import statsmodels.api as sm
import matplotlib.pyplot as plt

data = sm.datasets.co2.load_pandas().data

data = data.dropna()

data = data[(data.index >= '1958') & (data.index <= '1980')]

plt.figure(figsize=(10, 5))
plt.plot(data.index, data['co2'], label='CO2 concentration')
plt.title('Уровень CO2 (1958–1980 годы)')
plt.xlabel('Год')
plt.ylabel('Концентрация CO2 (ppm)')
plt.grid(True)
plt.legend()
plt.show()