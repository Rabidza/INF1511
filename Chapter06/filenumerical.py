f = open("numbers.txt", "w")
n = int(input("How many numbers? "))
print("Enter", n, "numbers")
for i in range(0, n):
    m = input()
    f.write("%s\n" %m)
f.close()

f = open("numbers.txt")  # NH: Default is read 'r'
lines = f.readlines()
f.close()

print("The numbers stored in the file are")
for line in lines:
    print(int(line),)  # NH: Why is the comma character needed in this line?

print("The numbers in the file multiplied by 2")
for line in lines:
    print(int(line) * 2)
