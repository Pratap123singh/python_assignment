try:
    with open("x_file",'x') as f:
        f.write("Pennch Tiger Reserve is in MP and Maharastra border.")
except FileExistsError:
    print("File already exits.")
