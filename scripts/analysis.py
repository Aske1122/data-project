import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

df = pd.read_csv("data/tips.csv")
df = df.dropna()

result = df.groupby("day")["total_bill"].mean().sort_values(ascending=False)

print(result)

result.to_csv("data/output.csv")

engine = create_engine("sqlite:///data/database.db")
df.to_sql("tips_data", engine, if_exists="replace", index=False)

result.plot(kind='bar')
plt.title("Average Bill by Day")
plt.show()

print("DONE")