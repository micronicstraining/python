
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

f = open("input.txt", "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                             # Note: if you want to write to the file use "w" as second argument

for line in f.readlines():   # read lines
    print each_line

f.close()                   # It's important to close the file to free up any system resources.

f1 = open("input1.txt", "r")

print only_first_line

# do not forget to close file!
