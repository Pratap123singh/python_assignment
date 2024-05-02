formula=input("Enter formula: ")
l=list(formula)
print(l)
open_bracket=['(','{','[','<']
close_bracket=[')','}',']','>']

for e in list(formula):
    print(e)
    formula.pop(e)
    print(formula)