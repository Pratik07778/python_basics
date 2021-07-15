name = input("enter your name ")
age = input("enter your age ")
city = input("enter your city ")
data = name+','+age+','+city+'\n'
print(data)

with open("user.csv",'a') as file:
    file.write(data)


# file.write("jdklfjsdfl")


