def changeName(cname):
    firstSpace = 0
    secondSpace = 0
    firstName = ""
    middleName = ""
    lastName = ""
    
    if (cname.find(" ") != -1):
        firstSpace = cname.index(" ")
        firstName = cname[0:firstSpace]
    if (cname.find(" ", firstSpace + 1) != -1):
        secondSpace = cname.index(" ",firstSpace + 1)
        middleName = cname[firstSpace + 1:secondSpace]
        lastName = cname[secondSpace + 1:]
        changedName = '{}, {}.{}.'.format(lastName,firstName[0],middleName[0])
    else:
        lastName = cname[firstSpace + 1:]
        changedName = '{}, {}.'.format(lastName,firstName[0])
        
    return changedName
    

name = input()
print(changeName(name))

