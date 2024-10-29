while (True):
     print("hi can you give me your password")
     password = input()
     if password == "password":
          print("correct")
          break
     else:
          print("try again")
print("Yay! you logged in")

count = 0
while (count < 3):
     print("yay i can count")
     count = count +1

shopping_list = ["milk", "eggs", "bread", "brownies"]
print(f"List before: {shopping_list}")
shopping_list.append("apples")
print(f"List after: {shopping_list}")
print(f"your list is {len(shopping_list)} long")
shopping_list.pop(1)
print(f"Removed last item in {shopping_list}")
length = len(shopping_list)
string = "your list is " + str(length) + " long"
print(string)
print(f"your list is {length} long")

#find the average of these numbers
numbers= [1,2,3,4,5,6,7,8,9,10,11,12,20]

sumOfNumbers= 0

for num in numbers:
     sumOfNumbers = sumOfNumbers+num
     # counter = counter +1
     
print(f"sum is {sumOfNumbers}")
avg = sumOfNumbers/len(numbers)
print(f"average is {avg}")