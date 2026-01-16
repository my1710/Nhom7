import pandas as pd

df = pd.read_excel("Online Retail.xlsx")
df.to_csv("online_retail.csv", index=False)
