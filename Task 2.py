a=input("Enter text to write to the file output.txt : ")
file=open("output.txt", "w")
(file.write(a))
file.close()

print("Data sucessfully written to output.txt")
print("")

b=input("Enter additional text to append : ")
file=open("output.txt", "a")
file.write("\n" + b)
file.close()

print("Data sucessfull appended")
print("")

print("Final content of the output.txt : ")
file=open("output.txt", "r")
print(file.read())
file.close()