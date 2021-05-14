f = open('E:\María\clases_keepcoding\Linkedin_courses\Python_Automation\Ex_Files_Python_Automation\Exercise Files\inputFile.txt','r')
PassFile = open('E:\María\clases_keepcoding\Linkedin_courses\Python_Automation\PassFile.txt','w')
FailFile = open('E:\María\clases_keepcoding\Linkedin_courses\Python_Automation\FailFile.txt','w')

for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        PassFile.write(line)
    else:
        FailFile.write(line)

#you can also type

'''for line in f:
       line_split = line.split()
       if line_split[2] == "P":
           '''


f.close()
PassFile.close()
FailFile.close()

 

