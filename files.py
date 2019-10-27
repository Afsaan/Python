# # how to create a file if the file doesnot exist

# # open("myfile.txt","xt")  # x means creating a new file and t means the text file

# # now how to write to a file

# f= open("myfile.txt","w")   # w means writting to a file
# f.write("python")
# f.write("is a")
# f.write("best programming language")


# # now appending to a file 

# f_app = open("myfile.txt",'a')
# f_app.write("and i love data science")

# f.close()  # its important to close a file before reading the file

# # reading the file
# f_read = open("myfile.txt","r")
# print(f_read.readline())

# deleting of file
import os
os.remove("myfile.txt")