# list1 = ["ten", "twenty", "third"]
# list2 = [10, 20, 30]
# list3 = [1, 2, 3]
# join = dict(zip(list1, list2))
# print(join)


"""
tuple1 = ("one", "two", "three")
tuple2 = (1, 2, 3)
join = dict(zip(tuple1, tuple2))
print(join)"""


# str1 = "my name is", "i am 19 year"
# str2 = "sourav", "old"
# join = dict(zip(str1, str2))
# print(join)

"""dict1 = {
    "ten" : 10,
    "twenty" : 20,
    "thirty" : 30,
}
dict2 = {
    "one" : 1,
    "tow" : 2,
    "three" : 3,
}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
dict2.update(dict1)
print(dict2)"""


# dict1 = {
#     "class" : {
#         "student" : {
#             "name" : "mike",
#             "subject" : {
#                 "phy" : 70,
#                 "math" : 80,
#                 "che" : 88,
#             }
#         }
#     }
# }
# print(dict1["class"]["student"]["subject"]["math"])


"""name = ["sourav", "nabi", "yash"]
details = {
    "work" : "bca",
    "salary" : 13000,
    "experience" : "10 year",
}
result = dict.fromkeys(name, details)
print(result)
if "work" in details.keys():
    print("present in dict")
else:
    print("not present in dict")
"""


# dict1 = {
#     "name" : "kelly",
#     "age" : 25,
#     "salary" : 12000,
#     "city" : "up",
# }
# dict1["location"] = dict1.pop("city")
# print(dict1)
# dict1["naam"] = dict1.pop("name")
# print(dict1)
# dict1["umer"] = dict1.pop("age")
# print(dict1)


"""dict2 = {
    "math" : 88,
    "sci" : 34,
    "phy" : 87,
    "che" : 98,
    "bio" : 70
}
print(max(dict2, key=dict2.get))
"""

# dict1 = {
#     "emp1" : {
#         "name" : "sourav",
#         "salary" : 9000,
#         "work" : "bca",
#     },
#     "emp2" : {
#         "name" : "nabi",
#         "salary" : 12000,
#         "work" : "d-pharma",
#     },
#     "emp3" : {
#         "name" : "yash",
#         "salary" : 11000,
#         "work" : "digital-marketing",
#     },
# }
# dict1["emp1"]["salary"] = 12000
# dict1["emp3"]["salary"] = 12000
# print(dict1)
# dict1["emp1"]["amount"] = dict1["emp1"].pop("salary")
# dict1["emp2"]["amount"] = dict1["emp2"].pop("salary")
# dict1["emp3"]["amount"] = dict1["emp3"].pop("salary")
# print(dict1)
# dict1["emp1"]["naam"] = dict1["emp1"].pop("name")
# dict1["emp2"]["naam"] = dict1["emp2"].pop("name")
# dict1["emp3"]["naam"] = dict1["emp3"].pop("name")
# print(dict1)


"""dict2 = {
    "math" : 88,
    "sci" : 34,
    "phy" : 87,
    "che" : 98,
    "bio" : 70
}
print(max(dict2, key=dict2.get))
"""

    
# student = {
#     "name" : "sourav rawat",
#     "subjects" : {
#         "phy" : 89,
#         "mth" : 98,
#         "che" : 90
#     }
# }
# new_dict = {
#     "city" : "up",
#     "name" : "yash chauhan",
# }
# print(student.keys())
# print(list(student.keys()))
# print(len(student))
# print(student.values())
# print(list(student.values()))
# print(student.items())
# pairs = (list(student.items()))
# print(pairs[1])
# print(student["name2"]) # error
# print(student.get("name2")) # not error
# student.update({"city" : "delhi"})
# print(student)
# student.update(new_dict)
# print(student)

 
"""collection = {1, 2, 3, 4, 4, "hello", "world", "hi", "hi"}
print(collection)
print(type(collection))
print(len(collection))"""


# collection = set()
# collection.add(2)
# collection.add(9)
# collection.add(2)
# collection.add("sourav")
# collection.add((5, 6, 5, 6))
# print(type(collection))
# print(collection)
# # collection.remove(9)
# print(collection)
# print(len(collection))
# collection.clear()
# print(len(collection))


"""collection = {"sourav", "rawat", "sonu", "age", "you"}
print(collection.pop())
print(collection.pop())"""


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.union(set2))
# print(set1)
# print(set2)
# print(set1.intersection(set2))


"""dictionary = {
    "cat" : "a small animal",
    # "table" : ["a piece of furniture", "list of facts & figures"]
    "table" : ("a piece of furniture", "list of facts & figures") 
}
print(dictionary)
"""

# sets = {"python", "c++", "java", "python", "javascript", "java", "python", "java", "c++", "C"}
# print(sets)
# print(len(sets))


# dict1 = {}
# x = int(input("enter phy :"))
# dict1.update({"phy" : x})
# x = int(input("ente che :"))
# dict1.update({"che" : x})
# x = int(input("enter math :"))
# dict1.update({"math" : x})
# print(dict1)


values = {9, "9.0", 9, 8, "Sourav", "rawat"}
print(values)
values2 = (
    {"float" : 9.0}, {"int" : 9}
)
print(values2) 




