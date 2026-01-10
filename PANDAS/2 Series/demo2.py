import pandas as pd

data = [10,20,40,80,100]
s = pd.Series(data, index=["A","B","C","D","E"])
print(s)

print("------------------------------")
print("\nvalue from a pandas series label A : ",s["A"],s["D"])