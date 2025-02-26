basicPay = float(input("Enter the basic pay of the employee : "))

# Calculating HRA

HRA = 0.1 * basicPay
TA = 0.05 * basicPay
totalSalary = basicPay + HRA + TA
professtionalTax = 0.02 * totalSalary
netSalary = totalSalary - professtionalTax

# Printing the result

print("The gross salary of the employee is : ",netSalary)


"""
Output :
(base) student@ioe-l1lab-06:~$ python 56salary.py
Enter the basic pay of the employee : 20000
The gross salary of the employee is :  22540.0

"""
