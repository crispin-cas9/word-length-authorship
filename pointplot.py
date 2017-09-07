# the graph

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

# Load the example exercise dataset
df = sns.load_dataset("exercise")

# Draw a pointplot to show pulse as a function of three categorical factors
g = sns.factorplot(x="time", y="pulse", hue="kind", data=df,
                   capsize=0, errwidth=0, palette="YlGnBu_d", size=6, aspect=.9)
g.despine(left=True)

plt.show()

# in the final -- x = "letters per word", y = "percent of total words", hue = "author"