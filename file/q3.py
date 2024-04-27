# 3. Write a Python program to append text to a file and display the text.

with open("file.txt", "a") as f:
    f.write("\n")
    f.write("i like to do cooking.")
f.close()
print("output of lines after appending.")
with open("file.txt","r") as f:
    print(f.read())
    
