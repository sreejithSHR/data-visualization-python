import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'./brithYearly.csv')
print(data) 

dataP = data.pivot("month", "year", "births")
print(dataP)

sns.heatmap(data, annot=True,fmt="d")

plt.show()