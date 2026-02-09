# create a function full_name(fname, lname) that return a string joined with a blank space

def full_name(fname, lname):
    return(fname + " " + lname)

fname = input("Enter your first name : ")
lname = input("Enter your last name : ")

print(full_name(fname,lname))