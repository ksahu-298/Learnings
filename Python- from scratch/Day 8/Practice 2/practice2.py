file = open("karan.txt", "x")
content = {"name": "Karan", 
           "course": "Python Programming"}
file.write(str(content))
file.close()