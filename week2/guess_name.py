# Program to guess a file name
file = open("file.txt")  # open a file
content = file.read()  # read file
guess = input("Please enter your guess ")  # guess the file contents


if guess == content:  # compare guess using if statement
    print("You guessed correctly :)")
else:
    print("Incorrect guess :(")
