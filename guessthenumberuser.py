import random
def guess(x):
    random_num=random.randint(1,x)
    user_num=0
    while random_num != user_num:
        user_num=int(input((f'enter the number between 1 and {x}')))
        if user_num<random_num:
            print("The number is small")
        elif user_num>random_num:
            print("the number is high")
    print(f"Yahoo! Guessed the number {random_num} is correct! CHEERS MATE!")
boom=int(input("Enter the number you want to search within the range(like if u want to search between 1 and 10 then enter 10)"))
guess(boom)