#---------- Q6. Write a program to check whether a number is prime. ----------


num = int(input("Enter a Number : "))

if num > 1:
    for i in range(2, num):
      if num % i == 0:    
         print("Not Prime")
         break
    else:
       print("Prime")
else:
   print("Not Prime")
