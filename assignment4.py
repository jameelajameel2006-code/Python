print("Assignment1:Number Analysis Program")
for i in range(1,11):
	if i%2==0: #2,4,6,8
		print(i,"=Even")
	else:
		print(i,"=Odd")
	if i%3==0: #3,6,9
		print("Divisable by 3")


print("Bonus Task:")
count=2
while count<=10:
	print("Count:",count)
	count+=2
	







print("Assignment2:Student Marks Analyzer")
passed=0
failed=0
highest=0
for i in range(1,6):
	marks=int(input(f"Enter marks of Student {i}:"))
	if marks>highest:
		highest=marks
	if marks>=80:
		grade=("A")
		passed=passed+1
	elif marks>=60:
		grade=("B")
		passed=passed+1
	elif marks>=50:
		grade=("C")
		passed=passed+1
	else:
		print("Fail")
		failed=failed+1
	print(f"Students {i}:{grade}")

print("Total passed:",passed)
print("Total failed:",failed)
print("Highest marks:",highest)