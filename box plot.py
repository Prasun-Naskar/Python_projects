import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
print(data.head())

#box plot
import matplotlib.pyplot as plt
plt.boxplot(data["Radio"])
plt.show()