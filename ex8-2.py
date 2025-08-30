with open("test.txt", 'a') as testFile:
    testFile.write("\nthis is a new line")
    testFile.write("\nnew line added")


with open("test.txt", 'r') as testFile:
    for line in testFile.readlines():
        print(line.strip())

with open("test.txt","r") as testFile:
    content = testFile.readlines()
    print(content)