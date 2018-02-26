months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
n = int(input("Enter a value between 1 and 12: "))

if 1 <= n <= 12:
    print("The month is", months[n - 1])
else:
    print("Value is out of range")
