Student={"Name":"Rama",
            "Age":20,
            "Height":5.6,
            "Address":"Kathmandu"
}
print(Student)
print(len(Student))
print(Student["Age"])
for i in Student:
    print(i)
for i in Student.keys():
    print(i)
for i in Student:
    print(Student[i])
for i in Student.values():
    print(i)
for i in Student:
    print(i," ",Student[i])
for i,j in Student.items():
    print(i," ",j)