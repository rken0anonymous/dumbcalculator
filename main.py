from Functions.addition import Addition
from Functions.division import Division
from Functions.multiplicaton import Multiplication
from Functions.subtraction import Subtraction

def main():
    print("Emter First Number")
    num1 = int(input())
    print("Enter Second Numbers")
    num2 = int(input())
    add = Addition.addition(num1, num2)
    sub = Subtraction.subtraction(num1, num2)
    mult = Multiplication.multiplication(num1,num2)
    div = Division.division(num1,num2)
    print(add)
    print(sub)
    print(mult)
    print(div)

main()