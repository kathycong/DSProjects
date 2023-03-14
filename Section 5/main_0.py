#Add a file in the in the system memory
newfile = open("Section 5/newfile.txt", "w+") #replace w+ with r for reading the file only. w+ refers to writing on the file

string = "This is the content that will be written to the text file."

newfile.write(string)