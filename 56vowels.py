
#checking vowels
char = input("Enter the character : ")

vowels = ['a', 'e', 'i', 'o', 'u',"A","E","I","U","O"]

if char in vowels:
    print(char, "is a vowel")

else:
    print(char, "is not a vowel")


"""
Output:
(base) student@ioe-l1lab-06:~$ Enter the character : e
e is a vowel

(base) student@ioe-l1lab-06:~$ Enter the character : d
d is a vowel
"""
