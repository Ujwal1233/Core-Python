emp={
    "Id":101,
    "Name":"John",
    "Age":30,
    "Address":"Bangalore"
}
print(emp)
print(type(emp))
print(emp["Name"])
print(emp.get("Age"))
print(emp["Address"])
emp["Mobile"]=1234567890
print(emp)
del emp["Mobile"]
print(emp)