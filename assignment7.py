print("List Operations (Intermidiate)")
num=[22,33,44,55,66,77]
print("List of Numbers",num)
print("Maximum numbers:")
print(max(num))
print("Minimum numbers:")
print(min(num))
print("Sum of all elements:")
print(sum(num))
print("Even numbers:")
for num in num:
	if num%2==0:
		print(num,"Even")





print("Assignment2:Tuple and Set Practice")
print("(Tuple):")
tuple=(22,42,45,44,67,)
print(tuple)
print(tuple.count(44))


print("(Set):")
set={2,5,2,8,5,9}
print(set)
set.add(10)
print("After add 10:")
print(set)

set.remove(5)
print("After remove 5: ")
print(set)