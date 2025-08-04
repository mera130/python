file1 = open("coding.txt", "r")
file2 = open("sample.txt", "w")

for x in file1.readlines():
    if not (x.startswith("coding")):
        print("/n the line without coding /n")
        print(x)
        
        file2.write(x)
        
file1.close()
file2.close()
        
        