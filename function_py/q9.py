def func(l1: list):
    for e in l1:
        for key in e:
            if key == "id":
                print(e)

l=[{1:"10", 2:"20"},{'id':"100"}]
func(l)

