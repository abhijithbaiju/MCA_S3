stud={
    "name":"Jo",
    "age":22,
    "course":"MCA",
    "mark":80
}

print("Dictionary:",stud)

print("Student Name:",stud["name"])

stud["College"]="Mangalam college of engineering"
print("college:",stud["College"])

print(stud)

stud["mark"]=90
print(stud)

del stud["age"]
print(stud)

print("keys:",stud.keys())

print("Values:",stud.values())


