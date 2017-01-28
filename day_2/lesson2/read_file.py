# go over tut. here 1st
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

# mode either r, w, a
# f = open("input.txt", "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
#                              # Note: if you want to write to the file use "w" as second argument
#
# for line in f.readlines():   # read lines
#     print(line)
#
# f.close()                   # It's important to close the file to free up any system resources.
#
f1 = open("input1.txt", "r")

print(f1.readline())
print(f1.readline())

f1.close()
