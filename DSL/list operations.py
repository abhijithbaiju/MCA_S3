num=[10,20,30,40,50]
print("Original list:",num)

num.append(60)
print("Append:",num)

num.insert(5,25)
print("Inserted:",num)

num.remove(30)
print("Removed",num)

num.sort()
print("sorted",num)

num.reverse()
print("Reverse",num)

print("Length of the array",len(num))

print("value",num[2])

num.pop(5)
print("Deleted",num)