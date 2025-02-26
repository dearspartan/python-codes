num1 = input("Enter a number : ")
totalDigit = 0
sum = 0

#counting number of digits
for digit in num1 :
    totalDigit = totalDigit + 1

 #print("The Total Number of digits in the given number is",totalDigit )

for digit in num1 :
    sum = sum + pow(int(digit),totalDigit)
    continue

num1 = int(num1)

if (num1 is sum) :
    print("The Number", num1,"is an armstong number" )
else :
    print("The Number", num1,"is not an armstong number")
    
