num1 = float(input("Enter first number: "))
num2 = float(input("enter second number: "))

# choose operation
print("Selection operation")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. Divide")

choice = input("enter choice (1/2/3/4): ")

# perform calculation
if choice == '1':
    print("result: ",num1 + num2)
elif choice =='2':
    print("result :", num1 -num2)
elif choice =='3':
    print("result :",num1*num2)
elif choice =='4':
    if num2 !=0:
        print("result: ",num1/num2)
    else:
        print("invalid input")






