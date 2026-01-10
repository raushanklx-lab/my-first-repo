import pandas as pd

data = {
    "Student" : ["Raushan", "John", "Ben"],
    "Rank" : [1,2,3],
    "Marks" : [98, 89, 76]
}

df = pd.DataFrame(data)

# high = df[df["Marks"] > 80 ]
# print(high)

avg = df["Marks"].mean()
print(avg)