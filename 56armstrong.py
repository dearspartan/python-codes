num = input("Enter a number : ")

length = len(num)

calculations = 0
temp = 0

for i in range(0,length) :
    temp = int(num[i])
    calculations = calculations + (temp**length)

if calculations == int(num) :
    print(num, " is an Amstrong number.")

else :
    print(num, " is not an Amstrong number.")


"""
Output:
(base) student@ioe-l1lab-06:~$ Enter a number : 153
153  is an Amstrong number.

(base) student@ioe-l1lab-06:~$ Enter a number : 123
123  is not an Amstrong number.
"""
