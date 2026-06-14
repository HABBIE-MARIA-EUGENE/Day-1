print("Hello World")

a = int(input("Enter a num "))
b = int(input("Enter another num "))
print(a)
print(b)

c = a+b
print("Sum is ",c)
print(f"Sum = {c}")

d = input("Enter your name: ")
print(f"Welcome back {d}")

age = int(input("Enter your age "))

if age>=18:
    print(f"Your are {age} years old, You can vote")
else:
    print(f"your are {age} years old and ineligible to vote")


f = int(input("Enter a num to check "))
if (f%2==0):
    print("Even")
else:
    print("Odd")





for i in range (10):
    print(i)

for i in range (1,10+1):
    print(i)

for i in range (1,11):
    print (f"2 x {i} = {2*i}")

