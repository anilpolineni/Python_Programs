# The following lines to take three numbers from user
num1 = int(input('enter the number:'))
num2 = int(input('enter the number:'))
num3 = int(input('enter the number:'))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The Maximun number is",num1,",",num2,"and",num3,"is",largest)
