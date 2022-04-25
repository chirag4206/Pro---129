import pandas as pd
import numpy as np

df=pd.read_csv("dwarf_stars.csv")


df=df[df["Mass"].notna()]
df=df[df["Radius"].notna()]

df["Mass"]=np.array(df["Mass"], float)

df["Radius"]=[element* 0.102763 for element in df["Radius"]]
df["Mass"]=[element* 0.000954588 for element in df["Mass"]]
df.to_csv("datamerge_final.csv")