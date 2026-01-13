#---------- Q5. Write a program to find the factorial of a number. ----------
# 5! = 5 x 4 x 3 x 2 x 1 =120

num = int(input("Enter a Number : "))
fact = 1
for i in range(1, num+1):
    fact *= i
    # print(i)
    # print(fact)
print(fact)

