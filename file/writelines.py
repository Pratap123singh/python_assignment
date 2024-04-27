
with open("file.txt","a") as f:
    l=["\n","India is a", " prismatic society."]
    f.writelines(l)
f.close()
print("-----------------------------------------------------------------------------")
with open("file.txt","r") as f:
    print(f.read())
