#---------- Q3. Count vowels in a string ----------

s = input("Enter a name / word / Sentence : ")
count = 0
for char in s.lower():
    if char in "aeiou":
        count += 1
print("Number of Vowel : ",count)


