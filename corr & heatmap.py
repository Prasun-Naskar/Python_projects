correlations =df.corr(method='pearson')
# Correlation Between All The Features
print(correlations)
# Correlation Between A Particular column "Year"
print(correlations["Year"])

# Visualizing Correlation
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(correlations)
plt.show()