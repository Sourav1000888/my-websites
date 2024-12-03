# tuple = (1, 4, 3, 5, 6, )
# print(tuple[:3])
# print(tuple[2:])
# print(tuple[3:len(tuple)])
# print(tuple.index(6))
# print(tuple.count(4))

# tuple = ("sourav", "nabi", "yash", "nihal", "govind")
# print(tuple.count('yash'))
# print(tuple.index("nabi"))
# print(tuple[2:4])

# list = [3, 5, 6, 1, 2, 9]
# list.append(444)
# print(list)
# print(list.count(3))
# list.extend([333, 444, 555])
# print(list)
# print(list.index(6))
# list.insert(0, 99)
# print(list)
# list.pop(3)
# print(list)
# list.remove(5)
# print(list)
# list.reverse()
# print(list)
# list.sort()
# print(list)

# list = [3, 6, 3, 1, 9, 0]
# a = list[0]
# list[0] = list[5]
# list[5] = a
# print(list)

"""list = ["sourav", "nabi", "yash", "nabi", "sourav"]
copy_list = list
copy_list.reverse()
if copy_list == list:
    print("palindrome")
else:
    print("not palindrome")
"""


# password = int(input("enter password :"))
# rev_password = int(input("enter again password :"))
# pass_key = 123456
# if password == pass_key:
#     if pass_key == rev_password:
#         print("correct password ")
#     else:
#         print("second password incorrect")
# else:
#     print("incorrect try again")


"""tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
sum = tuple1 + tuple2
print(sum)
exists = 5 in tuple2
print(exists)
print(type(tuple2))
# string = str(tuple2)
# print(type(string))
index = tuple2.index(5)
print(index)

list = [1,2, 5, 3, 7, 4]
tup = tuple(list)
print(type(tup))"""

# tuple = (4, 3, 7, 1, 9, 5 )
# print("max :", max(tuple))
# print("min :", min(tuple))


# tuple2 = ('h', 'e', 'l', 'l', 'o')
# result = ''.join(tuple2)
# print(result)
# tuple3 = (3, 4, 6, 1, 2)
# total = sum(tuple3)
# print(total)
# add = tuple(sorted(tuple3))
# print(add)


"""tup1 = (1, 2, 3)
tup2 = (3, 4, 5)
con = tuple(set(tup1).union(tup2))
print(con)
print(tup1[0])
print(tup1[-1]) 
print(tup2[-2])"""

# info = {
#     "key" : "count",
#     "name" : "sourav",
#     "learning" : "python",
#     "age" : 19,
#     "is_adult" : True,
#     "subject" : ["python", "c", "c++", "java"],
#     99 : 45.3,
#     88.12 : 000
# }
# print(info)
# print(type(info))
# print(info["key"])
# print(info["name"])
# print(info["learning"])
# print(info["age"])

# info["name"] = "suryansu"
# print(info["name"])
# info["surname"] = "rawat"
# print(info)

# nul_dict = {}
# nul_dict["name"] = "sourav"
# nul_dict["surname"] = "rawat"
# print(nul_dict)


"""student = {
    "name" : "sourav",
    "subject" : {
        "phy" : 88,
        "mth" : 98,
        "che" : 79
    }
}
print(student)
print(student["subject"]["phy"])
"""

# tup1 = (2, 4, 7, 2, 1)
# tup2 = (1, 3, 5, 6)
# total = sum(tup1)
# print(total)
# sort = sorted(tup1)
# print(sort)
# mx = max(tup1)
# mn = min(tup1)
# print(mx, mn)
# print(tup1[0],tup1[-1])
# add = tuple(set(tup1).union(tup2))
# print(add)
# sum = tup1 + tup2
# print(sum)

"""tup1 = ('h', 'e', 'l', 'l', 'o')
tup2 = ('w', 'o', 'r', 'l', 'd')
tup3 = ('s', 'o', 'u', 'r', 'a', 'v')
sum = tup1 + tup2
print(sum)
join = ''.join(tup1)
join1 = ''.join(tup2)
join3 = ''.join(tup3)
add = join + " " + join1 + " " + join3
print(add)
"""

# student = {
#     "name" : "sourav",
#     "sur name" : "rawat",
#     "age" : 19,
#     "subject" : {
#         "math" : 78,
#         "pht" : 88,
#         "che" : 79,
#         "bio" : 90
#     },
#     "result" : {
#         "pass" : "yes",
#         "fail" : "no"
#     },
#     "cgpa" : 8.9,
#     "language" : {
#         "HTML" : "done",
#         "CSS" : "done",
#         "JavaScript" : "no",
#         "React.js" : "no",
#     }
# }
# print(student)
# print(student["result"])
# print(student["language"]["CSS"])

# name = input("enter name :")
# name2 = "rawat"
# add = name + name2
# name3 = (input("enter name again :"))
# check = add == name3
# print(check)


"""list1 = ['name', 'age', 'class']
list2 = ['sourav', '19', 'bca']
create_d = dict(zip(list1, list2))
print(create_d)
"""

# dict1 = {
#     "ten" : 10,
#     "twenty" : 20,
#     "thirty" : 30,
# }
# dict2 = {
#     "one" : 1,
#     "two" : 2,
#     "three" : 3,
# }
# dict3 = { **dict1, **dict2}
# print(dict3)

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)



"""simple_dict = {
    "class" : {
        "student" : {
            "name" : "mike",
            "marks" : {
                "physics" : 70,
                "history" : 80
            }
        }
    }
}
print(simple_dict["class"]["student"]["marks"]["history"])
"""

# emp = ["kelly", "emma"]
# defaults = {"designation": 'developer', "salary": 8000}
# res = dict.fromkeys(emp,defaults)
# print(res)


"""dict1 = {
    "name" : "sourav",
    "age" : 19,
    "salary" : 90000,
    "city" : "new york",
}
key = ["name", "salary"]
if 19 in dict1.values():
    print("sourav preseent in dict")
    """

# dict1 = {
#     "name" : "kelly",
#     "age" : 25,
#     "salary" : 8000,
#     "city" : "new york",
# }
# dict1["location"] = dict1.pop("city")
# print(dict1)


"""dict2 = {
    "phy" : 82,
    "math" : 65,
    "history" : 75,
}
print(min(dict2, key=dict2.get))
"""

dict1 = {
    "emp1" : {
        "name" : "jhon",
        "salary" : 7500,
    },
    "emp2" : {
        "name" : "emma",
        "salary" : 8000
    },
    "emp3" : {
        "name" : "brad",
        "salary" : 500
    },
}
dict1["emp3"]["salary"] = 8500
print(dict1)
