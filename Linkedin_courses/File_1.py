#We have a file (.txt) containing student marks.

#Let's start by opening a .txt file that we want just to read. Important not to forget 'r' as 'read'.
f = open('E:\María\clases_keepcoding\Linkedin_courses\Python_Automation\Ex_Files_Python_Automation\Exercise Files\inputFile.txt','r')

#We will also open two more files to write on, and where we will separate passed and failed exams. Important not to forget 'w' as 'write'
PassFile = open('E:\María\clases_keepcoding\Linkedin_courses\Python_Automation\PassFile.txt','w')
FailFile = open('E:\María\clases_keepcoding\Linkedin_courses\Python_Automation\FailFile.txt','w')

#We will paste passed exams in our 'PassFile' and failed exams in 'FailFile'.
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        PassFile.write(line)
    else:
        FailFile.write(line)

#you can also type

'''for line in f:
       if 'P' in line:
           PassFile.write(line)
        else:
            FailFile.write(line)
           '''


f.close()
PassFile.close()
FailFile.close()

 

