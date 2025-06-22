import pandas as pd
import os

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

os.makedirs("Data", exist_ok=True)
df.to_csv("Data/people.csv", index=False)