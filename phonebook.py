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
    
    print (phonebook)
    return phonebook
     
def menu():
    print("...................................................................")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("................................................................................")
    
    print("\tYou can now perform the following operations on this phonebook\n")

    print("1. Add a new contact")

    print("2. Remove an existing contact")

    print("3. Delete all contacts")

    print("4. Search for a contact")

    print("5. Display all contacts")

    print("6. Exit phonebook") 
    
    choice = int(input("enter your choice"))
    return choice

def addcontact(pb):
    dip = []
    
    for i in range(len(pb[0])):
        
        if i == 0:
            dip.append(str(input("enter a name")))
            
        if i == 1:
            dip.append(int(input("enter a phone number")))
        for i == 2:
            dip.append(str(input("enter an email address")))
        for i == 3:
            dip.append(str(input("enter date of birth dd/mm/yy")))
        for i == 4:
            dip.append(str(input("category family/friend/others")))
    
    pb.append(dip)
    return (pb)

def remove_existing(pb):
    query=str(input("enter the name of the contact you want remove"))
    
    temp = 0
    
    for i in range(len(pb)):
        if query == [pb][0]:
            temp= temp+1
            
            print(pb.pop(i))
            print("this contact has been removed ")
            return pb
        
        if temp ==0:
            print("sorry you have entered an invalid query ")
        
        
def remove_all(pb):
    return pb
    
    
        
        
    
    
    


                    
    
                
        
    
    
     