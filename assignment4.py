name=input("Enter name:")
age=int(input("Enter age:"))
exam_score=int(input("Enter exam score:"))
family_income=float(input("Enter family income:"))

if age<16:
	print("Sorry,too young.")
elif exam_score<60:
	print("Exam_score too low.")
 

if family_income<30000:
	decision="Admitted with full scholarship"
elif family_income<80000:
	decision="Admitted with partial scholarship"
else:
	decision="Admitted without scholarship"

print(name,decision)


num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("Before swap:")
print(("a="),num1)
print(("b="),num2)



