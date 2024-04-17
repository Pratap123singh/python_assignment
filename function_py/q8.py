def func(l1: list):
    count=0
    for e in l1:
        if e.count("s") == 2:
            print(e)
l1=["abcd","ssqw","acd","seds"]
func(l1)