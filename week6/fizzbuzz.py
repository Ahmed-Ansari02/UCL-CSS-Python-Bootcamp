def fizz_buzz(n):
    for number in range(1, n+1):
        if number % 5 == 0 and number % 3 == 0:
            print("fizzBuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("Buzz")
        
        else:
            print(number)
            
fizz_buzz(15)