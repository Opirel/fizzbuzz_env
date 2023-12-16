"""
fizz-buzz
if divide by 3 -fizz
if divide by 5- buzz
if divide by 3 and 5- fizzbuzz
"""
from icecream import ic

def FindEven():
   for num in range(1,101):
       if (num %2==0): ic(num)

def FindOdd():
    for num in range(1,101):
        if num %2 !=0: ic(num)





def FizzBuzz():
    for num in range(1,101):
        if (num % 5==0 and num % 3== 0): ic ("fizzbuzz")
        elif (num %5 == 0): ic("buzz")
        elif (num %3 == 0):ic("fizz")
        else:ic(num)

def main():
    
    FizzBuzz()
    # FindEven()
    #  FindOdd()


if __name__ == "__main__":
    main()