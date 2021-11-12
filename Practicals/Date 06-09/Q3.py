#Q3. WAP to read the integers till -1 is entered, then count and display the number of positive, negative
#and zeros entered.

pos=0
neg=0
zero=0
num_str = input("Input an integer (-1 terminates):")
num=int(num_str)

while num !=-1:
   if (num > 0):
       pos+=1
   elif (num < 0):
       neg+=1
   else:
       zero+=1
   num_str = input("Input an integer (-1 terminates):")
   num = int(num_str)

print("")
print("Sum of positive numbers: ", pos)
print("Number of negative nos: ", neg)
print("number of zeros entered: ", zero)