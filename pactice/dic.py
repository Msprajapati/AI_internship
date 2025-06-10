#Dictionary and sets
info={
    "key": "value",
    "name": "apnacollege",
    "learning" :"coding",
    "age": 35,
    "is_adult": True,
    "marks": 94.4,
    
}
#print(info)
#tuple ko key bna skte he dic or list ko key nhi bna skte
#print(info["name"])
info["name"]="mahendra"
info["surname"]="singh"
#print(info)


student={
    "name":"rahul kumar",
    "subjects":{
        "phy":97,
        "chem" : 98,
        "math": 95
    }
}
#print(student["subjects"]["chem"])

#print(student.keys())
print(student.values())
