def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


squar = int(input("Enter a number for squar: "))
square_num = squar * squar
print(f"{square_num} is squar of {squar}")
number = int(input("Enter a number to check it is odd or even: "))
odd_even(number)
