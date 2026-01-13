#---------- Q1.Find the largest number in a list ----------

# list = [23, 2, 32, 24, 243]
# print(max(list))

list = [23, 2, 32, 24, 243]
largest = list[0]

for i in list:
    if i > largest:
        largest = i

print("largest number : ", largest)
