# ===== FILE HANDLING TASKS =====

with open("coding.txt", "r") as file:
    content = file.read()  
    lines = content.splitlines() 


print("=== Entire File Content ===")
print(content)

print("\n===First 10 Characters ===")
print(content[:10])  


print("\n=== First Line ===")
print(lines[0] if lines else "File is empty!")


print("\n=== First Four Lines ===")
for line in lines[:4]:  
    print(line)

print("\n=== all Lines ===")
for line in lines:
    print(line)
    

