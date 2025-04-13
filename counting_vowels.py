# pROGRAM TO COUNT VOWELS

str1 = (input("Enter a Word:"))
vowels = ["a", 'e', 'i', 'o','u']
str2 = str1.lower()
vowelCount = 0
for char in str2:
    if char in vowels :
        vowelCount +=1

print("The number of vowels in the given word is ",vowelCount,".")
