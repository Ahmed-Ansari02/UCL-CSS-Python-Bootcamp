#Program to guess a file name
file = open("file.txt") 
content = file.read() 
guess = input("Please enter your guess ")  
if guess == content: 
    print("You guessed correctly :)")
else:
    print("Incorrect guess :(")