import json
employees = {

"employee1":{
  "employee_id": "AA-0001",
  "employee_name": "Ram",
  "employee_age":25,
  "employee_role": "developer",
  "mob_number" :"9080654389"
},
"employee2":{

 "employee_id": "AA-0002",
  "employee_name": "Priya",
  "employee_age":34,
  "employee_role": "Analyst",
  "mob_number" :"8098432190"   
},
"employee3":{
    
     "employee_id": "AA-0003",
  "employee_name": "Kavi",
  "employee_age":39,
  "employee_role": "software engineer",
  "mob_number" :"8904567832"   
},

"employee4":{

 "employee_id": "AA-0004",
  "employee_name": "Raj",
  "employee_age":42,
  "employee_role": "Product manager",
  "mob_number" :"9080754321"   
},

"employee5":{
 "employee_id": "AA-0005",
  "employee_name": "rahu",
  "employee_age":32,
  "employee_role": "HR-manager",
  "mob_number" :"7658904356"   
},

"employee6":{
 "employee_id": "AA-0006",
  "employee_name": "Janani",
  "employee_age":27,
  "employee_role": "Designer",
  "mob_number" :"9079690432"   
},

"employee7":{
 "employee_id": "AA-0007",
  "employee_name": "Jagan",
  "employee_age":22,
  "employee_role":"intern",
  "mob_number" :"9578904321"   
},

"employee8":{
 "employee_id": "AA-0008",
  "employee_name": "Mani",
  "employee_age":40,
  "employee_role": "salesmanager",
  "mob_number" :"9865922314"   
},

"employee9":{
 "employee_id": "AA-0009",
  "employee_name": "Rithu",
  "employee_age":21,
  "employee_role": "intern",
  "mob_number" :"9855922034"   
},

"employee10":{
 "employee_id": "AA-0010",
  "employee_name": "Prabhu",
  "employee_age":33,
  "employee_role": "intern",
  "mob_number" :"9855522100"   
}
}
new=json.dumps(employees)
print(new)


