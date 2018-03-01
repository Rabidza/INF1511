import sys


try:
    f = open("aboutbook1.txt", "r")
    lines = f.read()
except IOError:
    print("File aboutbook1.txt does not exist")
    sys.exit(1)
f.close()
print(lines)
