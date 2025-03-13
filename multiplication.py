#multiplication tables
n = int(input("Enter a number : "))

print("The multiplication table of {} is:".format(n))
for i in range(1,11):
    print("{}x{}={}".format(n,i,n*i))


