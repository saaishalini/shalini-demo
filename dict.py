#dict
newdict =	{
  "name": "shalini",
  "age": "21",
  "year": 2001
}
print(newdict)
#modify year
newdict =	{
  "name": "shalini",
  "age": "21",
  "year": 2001
}
newdict["year"] = 2018
print(newdict)

#add items
newdict =	{
  "name": "shalini",
  "age": "21",
  "year": 2001
}
newdict["clg"] = "shanmugha"
print(newdict)

#nested dictionary
students = {
  "stu1" : {
    "name" : "saran",
    "year" : 2004
  },
  "stu2" : {
    "name" : "Kavin",
    "year" : 2007
  },
  "stu3" : {
    "name" : "jeevi",
    "year" : 2011
  }
}

print(students)
#nested dictionary using clear()
students = {
  "stu1" : {
    "name" : "saran",
    "year" : 2004
  },
  "stu2" : {
    "name" : "Kavin",
    "year" : 2007
  },
  "stu3" : {
    "name" : "jeevi",
    "year" : 2011
  }
}

students.clear()
print(students)