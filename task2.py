import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_json(r'./rain.json')

plt.figure(figsize=(15,5))
plt.plot( df['Month'], df['Temperature'], lable='Temperature')
plt.show()


plt.figure(figsize=(17,5))
plt.plot( df['Month'], df['Rainfall'], lable='Rainfall')
plt.show()


plt.plot( df['Month'], df['Rainfall'], label='Rainfall')
plt.plot( df['Month'], df['Temperature'], lable='Temperature')
plt.legend()
plt.show()



