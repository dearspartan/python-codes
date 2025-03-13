num1 = int(input("Enter first number : "))  # User input 
num2 = int(input("Enter second number : "))

print("Before Swapping:")

print(f"1st Number = {num1}")
print(f"2nd Number = {num2}")

# Swapping using temp variable
temp = num1
num1 = num2
num2 = temp

print("After Swapping:")

print(f"1st Number = {num1}")
print(f"2nd Number = {num2}")
