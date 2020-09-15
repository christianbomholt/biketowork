import pandas as pd

data = pd.read_csv("data.csv")

df = data.T
df.columns = list(data.T.loc['Unnamed: 0'])
df =df.drop('Unnamed: 0',axis=0)

dft = df.cumsum()
# ["Day "+ str(x+1) for x in range(20)]
dft["date"] = pd.date_range(start='9/1/2020', end='9/20/2020')
# dft["id"] = list(range(20))
dft = dft.drop("0")
dft.head()

dt = pd.melt(dft, id_vars=['date'])
dt["category"] = dt["variable"]
dt.columns = ["date","name","value","category"]

dt[["date","name","category","value"]].to_csv("biking.csv",index=False)