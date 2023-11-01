user_input = input("Enter something for Python to echo back: ")
print(user_input)

# user convertion to int
user_input = input("Enter a number you want squared: ")
number = int(user_input)
print(number ** 2)

#while loop
name = None

while name != "your name":
    name = input("Please type your name: ")

print("Finally!")

#break
word = "hello"

for char in word:
    if char in "aeiou":
        continue
    print(char)

print("done")

#str formatting mini language
message = "you move me!"
print(f"{message:>20}")
