def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    
    
number = int(input("Enter a number: "))
odd_even(number)



def check(n):
      
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Equal to zero")

n = int(input("Enter the number: "))
check(n)

n = int(input("enter the number:))
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)
