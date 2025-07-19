import sys


def initial_phone_book():
    rows,cols =int(input("enter the initial number of contact"))
    
phone_book = []
print(phonebook)

for i in range(rows):
    print("/n enter the contat %d in the following the order only:" %(i+1))
    print("note: indication are mandatory")
    print
    ("......................................................................................")
    
    temp = []
    for j in range(cols):
        
        if j==0:
            temp.append(str(input("enter your name * :")))
            
            if temp[j] == '' or temp[j] == ' ':
                sys exit("name is mandatory field. process is executing due to blank field")
                
            if j == 1:
                temp.append(int(input("enter the number * :")))
                
            if j == 2 :
                temp.append(str(input("enter an email address")))
                
                if temp[j] == '' or temp[j] = ' ':
                    temp[j] = "none"
                    
            if j == 3:
                temp.append(str(input("enter your birthday(dd/mm/yy)")))
                
                if temp[j] == '' or temp[j] = ' ':
                    temp[j] = "none"
                    
            if j == 4:
                temp.append(str(input("category family/friends/work/other")))
                if temp[j] == '' or temp[j] = ' ':
                    temp[j] = "none"
    
    phonebook.append[temp]
                    
    
                
        
    
    
     