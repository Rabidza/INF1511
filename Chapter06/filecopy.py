f = open("aboutbook.txt", "r")
lines = f.read()
f.close()

g = open("copyaboutbook.txt", "w")
g.write(lines)
g.close()

print("The copy of the file is made")
g = open("copyaboutbook.txt", "r")
lines = g.read()
print(lines)
g.close()
