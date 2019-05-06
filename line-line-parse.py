

ins = open("file.txt", "r+") 
final = ""
for line in ins:
    linepart = int(line[:-1])

    num = "{0:b}".format(linepart)

    print("len num = ",len(num))

    newline = (str(num) + "\n").rjust(9,"0")
    
    final+=newline

ins.close()

f = open("file.txt", "w")
f.write(final)