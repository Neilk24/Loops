String1 = input("Please enter any string: ")
String2 = ('')

for x in String1:
    String2 = x + String2

print("\nThe original string was ", String1)
print("The reversed string is ", String2)