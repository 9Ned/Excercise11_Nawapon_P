numStep = int(input("Enter Number: "))
for x in range(numStep):
    for y in range(x+1):
        text = ""
        space = ""
        space = space + str(" "*(numStep-y-1))
        text = text + "*" * ((2*y)+1)
    print(space+text)