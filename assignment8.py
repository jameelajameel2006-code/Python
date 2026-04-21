print("Assignment 1: Students Marks Dictionary")
data={
	  "Jameela":90,
	  "Javeria":70,
	  "Qissa":60
}

print(data)
print("All students name:")
print(data.keys())
print("All marks:")
print(data.values())

highest_marks=max(data.values())
print("Highest marks is:",highest_marks)

print("Students with highest mark is :")
for name in data:
	if data[name]==highest_marks:
		print(name,"-",data[name])





print("Assignment 2:Product Price Manager")
products={
	      "Milk":150,
	      "Bread":80,
	      "Eggs":200
}

print("All Products:")
print(products)



print("All Products with Prices:")
for name,price in products.items():
	print(name,":",price)


products["Butter"]=250
print("After Adding New Item:")
print(products)


products["Milk"]=170
print("After Updating Milk Price:")
print(products)


total=sum(products.values())
print("Total Price Of All Products:",total)


