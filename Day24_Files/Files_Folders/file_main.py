with open("test.txt", mode="w") as file:
    file.write("Testing")

with open("test.txt") as file:
    print(file.read())


#Absolute file path
# root - /
# work - /work
#report file - /work/report.doc
#project - /work/project
#talk file - /work/project/talk.ppt
#__________
#Relative file path ../report.doc
#Working directory  > ./talk.ppt

# one dot for same working directory
# two dots to go one level up from the working directory