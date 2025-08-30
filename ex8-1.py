file = open("test.txt", 'w')
file.write("This is a test.\n")
file.write("Hello World\n")

file.write("I'm Saeed")
file.close()


with open("test.txt", 'r') as testFile:
    content = testFile.read()
    print(content)

with open("test.txt", 'r') as testFile2:
    for txtLine in testFile2.readlines():
        print(txtLine)