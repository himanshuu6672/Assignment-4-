file = "sample.txt"

if file == "sample.txt":
    file=open("sample.txt", "r")
    print(file.read())
    file.close()
else:
    print("Error : The file 'sample.txt' does not exist")