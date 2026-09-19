##DICTIONERY AND SET
# info={
#     "key":"value",
#      "name":"khagendra",
#      "course":"coding",
#      "age":20,
#      "marks": 34.5,
#      "is_adult":True,
#      "subjects":["FoSC","MCCT"],
#      "python":("easy language","fast learning","easy to understand")

# }

# info["marks"]=[89.9]
# print(info)
# print(type(info))
# print(info["name"])
# print(info["course"])

#CREATE NULL DICTIONERY
# null_dict={}
# print(null_dict)
# null_dict["name"]=["khagendra"]
# print(null_dict)

##NESTED DICTIONERY
# students={
#     "name":"khagendra",
#     "subjects": { 
#         "FoSC":"passed",
#         "MCCT": 89 },
#     "course":"BSC"
# }
# print(students)
# print(students["subjects"]["MCCT"])


#DICTIONERY METHODS
students={
    "name":"khagendra",
    "subjects": { 
        "FoSC":"passed",
        "MCCT": 89 },
    "course":"BSC"
}
# print(students.keys())
# print(list(students.keys()))
# print(len(list(students.keys())))
# print(len(students))

# print(students.values())
# print(list(students.values()))
# print(len(list(students.values())))

# print(students.items())
# print(list(students.items()))
# pairs=list(students.items())
# print(pairs[0])

# print(students["name"])
# print(students.get("name"))
# print(students["name1"])        ##will show error
# print(students.get("name1"))    ##will display NONE

# students.update({"city":"kathmandu","age":20.5,"gender":"male"})
# print(students)


#SET IN PYTHON
# collection={1,2,3,4,5,"hey you",23.3,False,2,6}
# print(collection)
# print(type(collection))
# print(len(collection))

# #empty set
# collection=set()
# print(type(collection))

 ##SET METHODS
 #sets are mutable, sets are immutable.

# set1=set()
# set1.add(1)
# set1.add(1)
# set1.add("khagendra")
# set1.add("rawal")
# print(set1)
# set1.remove("rawal")
# print(set1)
# set1.add(("ram","shyam",23))
# print(set1)
# set1.clear()
# print(len(set1))

# collection={"hello","how",23, "are","you"}
# print(collection.pop())
# print(collection.pop())

set1={1,2,3,4}
set2={2,3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))