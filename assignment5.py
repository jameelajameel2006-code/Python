
name=input("Enter your name:")
num=int(input("Enter a number:"))

if num%2==0:
	print("Even")
else:
	print("Odd")
print("Numbers from 1 to 5:")
for i in range(1,5):
	print(i)

print("Countdown:")
i=num
while i>=1:
	print(i)
	i=i-1

print("Thank you",name)