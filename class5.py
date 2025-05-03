# Print numbers from 1 to 100.

i = 1
while i <=100:
    print(i)
    i = i+1


# Print numbers from 100 to 1.
i = 100
while i>=1:
    print(i)
    i = i-1


# Print the multiplication table of a number n.
num = int(input("Enter the number: "))
i = 1
while i<= 10:
    number = num * i
    print(f"{num} x {i} = {number}") 
    i = i+1


# Print the elements of the following list using a while loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
List = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
while i < len(List):
    print(List[i])
    i = i+1


# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
Tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
num = int(input("Search for a number: "))

found = False
i = 0

while i < len(Tuple):
    if Tuple[i] == num:
        found = True
        break
    i = i+1

if found:
    print(f"The {num} are found in these Tuple")
else:
    print(f"The {num} are not found in these Tuple")
    

# Print the elements of the following list using a for loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
List = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for i in List:
    print(i)


# Search for a number x in this tuple using for loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

Tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
num = int(input(f"Search for a number in this tuple: "))
found = False
for i in range(len(Tuple)):
    if Tuple[i] == num:
        found = True
        break
if found:
    print(f"The {num} are found in these Tuple")
else:
    print(f"The {num} are not dound in these Tuple")
    
    
# Print number from 1 to 100
for i in range(1, 101):
    print(i)


# Print number from 100 to 1
for i in range(100, 0, -1):
    print(i)
   
   
# Print a multiplication table of a number n. 
num = int(input("Enter the number: "))
for i in range(1, 10+1):
    result = num*i
    print(f"{num} x {i} = {result}")
    