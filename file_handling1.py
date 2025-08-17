import os
with open("my_file.txt", "w") as file:
    file.write("Hello! My name is mehrish.")

with open("my_file.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("\nAll words in the file:")
    print(words)


print("\nChecking if My_file exists:")
if os.path.exists("My_file"):
    print("My_file exists")
else:
    print("My_file does not exist")


if not os.path.exists("My_file"):
    with open("My_file", "w") as file:
        file.write("Hello! This is my introduction in My_file.")
    print("\nCreated My_file")
else:
    print("\nMy_file already exists")

if os.path.exists("sample_doc"):
    os.remove("sample_doc")
    print("\nDeleted sample_doc")
else:
    print("\nsample_doc does not exist")

