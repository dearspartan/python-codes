num = input("Enter a number : ")

sum = 0

for digit in num :

    sum += int(digit)
    continue

print("The sum of the digits of the number is : ", sum)

"""
Output:
(base) student@ioe-l1lab-06:~$ Enter a number : 223
The sum of the digits of the number is :  7

(base) student@ioe-l1lab-06:~$ Enter a number : 333
The sum of the digits of the number is :  9
"""
