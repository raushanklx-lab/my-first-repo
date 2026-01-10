#CONCATENATE PANDAS DATAFRAME

import pandas as pd

data1 = {
    "student":["Ayush","Raushan","Manish","Tim","Baby"],
    "marks":[95,99,95,86,75],
    "Roll":["S01","S02","S03","S04","S05"]
}

data2 = {
    "student":["Kane","David","Ben","Gim","Hogward"],
    "marks":[87,76,59,69,86],
    "Roll":["S06","S07","S08","S09","S10"]
}

dataframe1 = pd.DataFrame(data1, index=["A","B","C","D","E"])
#print(dataframe1)

dataframe2 = pd.DataFrame(data2, index=["F","G","H","I","J"])
#print(dataframe2)

resdf =pd.concat([dataframe1,dataframe2])
print(resdf)