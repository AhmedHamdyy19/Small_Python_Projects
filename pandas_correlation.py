import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('whisky.csv')
flv = data.iloc[:, 2:14]
correlation_matrix = pd.DataFrame.corr(flv)

plt.figure()
plt.pcolor(correlation_matrix)
plt.colorbar()
plt.show()
