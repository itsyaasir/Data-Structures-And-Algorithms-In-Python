def calculate_gcd(dividend, divisor):
    if divisor == 0:
        return dividend
    else:
        return calculate_gcd(divisor, dividend % divisor)


def cleanNum():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    while type(num1 and num2) != int:
        print("Please enter a valid number")
        main(num1,num1)

def main(num1,num2):
    print("The GCD of {0} and {1} is {2}".format(
        num1, num2, calculate_gcd(num1, num2)))


cleanNum()