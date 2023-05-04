#creating a list
students=["shalini","saranya","priya","sangeetha"]
print(students)

#print using index value
print(students[3])

#slicing method
print(students[:2])

#add list items using append
students = ["shalini", "saranya", "priya","sangeetha"]
students.append("nivetha")
print(students)

#add list items using insert
students = ["shalini", "saranya", "priya","sangeetha"]
students.insert(2,"saran")
print(students)
 
 #add list items using extend

students = ["shalini", "saran", "sangi"]
staff = ["sathya", "anand", "priya"]
students.extend(staff)
print(students)


#remove list items

#remove particular item 
students = ["shalini", "saranya", "priya","sangeetha"]
students.remove("priya")
print(students)

#remove particular item using index
students = ["shalini", "saranya", "priya","sangeetha"]
students.pop(3)
print(students)
#using dek keyword
students = ["shalini", "saranya", "priya","sangeetha"]
del students[0]
print(students)

#loop comprehension

students = ["shalini", "saranya", "priya","sangeetha"]
newlist = []

for x in students:
  if "p" in x:
    newlist.append(x)
print(newlist)




 




