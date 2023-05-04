#with open("myfile.txt")as file:
   ##print(file.closed)

#different directory
#with open("C:\\Users\\HP\\Desktop")as file:
    ##print(file.closed)

#write
txt="hiiii shalini"
with open("myfile.txt",'w')as file:
    file.write(txt)


#writem using append

txt="hiiii shalini"
with open("myfile.txt",'a')as file:
    file.write(txt)




