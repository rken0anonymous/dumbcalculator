
from addition import addition
from subtraction import subtraction
from multiplicaton import multiplication
from division import division


def main():
    print("Emter First Number")
    num1 = int(input())
    print("Enter Second Numbers")
    num2 = int(input())
    add = addition(num1, num2)
    sub = subtraction(num1, num2)
    mult = multiplication(num1,num2)
    div = division(num1,num2)
    print(add)
    print(sub)
    print(mult)
    print(div)


main()