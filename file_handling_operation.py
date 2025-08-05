with open('conding.txt' , 'w') as file:
    file.write("hello this is mehrish")
    file.close()
    
with open('coding.txt' ,'r') as file:
    data = file.readlines()
    
    print("spilting the lines split() function")
    
    for line in data:
        word = line.split()
        print(word) 
        
file.close()


        
    
    