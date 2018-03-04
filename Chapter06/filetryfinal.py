import sys

try:
    f = open("Test.txt", "r")
    try:
        lines = f.read()
    finally:
        f.close()
except IOError:
    print("File test.txt does not exist")
    sys.exit(1)
