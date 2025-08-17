# open the file in read mode
file_read = open('sample.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# write in the file
file_write = open('sample.txt', 'w')
file_write.write(" File in write mode .......................")
file_write.write("Hi! this is mehrish ")
file_write.close()

# open the file in append mode
file_append = open('sample.txt', 'a')
# append in the file
file_append.write("\n File in append mode ................................")
file_append.write("Hi! this is mehrish")
file_append.close()