import pandas as pd
import matplotlib.pyplot as plt

data = [10, 20, 30, 40, 50]

df = pd.DataFrame(data, columns=["Values"])

print("Summary Statistics:")
print(df.describe())

plt.plot(df["Values"])
plt.title("Sample Data Visualization")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()
